import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
np.random.seed(seed=42)

# Create data
classA = np.array([[1, 1.5, 1.7, 1.45, 1.1, 1.6, 1.8],
                   [1.8, 1.55, 1.45, 1.6, 1.65, 1.7, 1.75]])
classB = np.array([[0.1, 0.5, 0.25, 0.4, 0.3, 0.6, 0.35, 0.15, 0.4, 0.5, 0.48],
                   [1.1, 1.5, 1.3, 1.2, 1.15, 1.0, 1.4, 1.2, 1.3, 1.5, 1.0]])
classC = np.array([[1.5, 1.55, 1.52, 1.4, 1.3, 1.6, 1.35, 1.45, 1.4, 1.5, 1.48, 1.51, 1.52, 1.49, 1.41, 1.39, 1.6, 1.35,
                    1.55, 1.47, 1.57, 1.48,
                    1.55, 1.555, 1.525, 1.45, 1.35, 1.65, 1.355, 1.455, 1.45, 1.55, 1.485, 1.515, 1.525, 1.495, 1.415,
                    1.395, 1.65, 1.355, 1.555, 1.475, 1.575, 1.485],
                   [1.3, 1.35, 1.33, 1.32, 1.315, 1.30, 1.34, 1.32, 1.33, 1.35, 1.30, 1.31, 1.35, 1.33, 1.32, 1.315,
                    1.38, 1.34, 1.28, 1.23, 1.25, 1.29,
                    1.35, 1.355, 1.335, 1.325, 1.3155, 1.305, 1.345, 1.325, 1.335, 1.355, 1.305, 1.315, 1.355, 1.335,
                    1.325, 1.3155, 1.385, 1.345, 1.285, 1.235, 1.255, 1.295]])

# Plot the data
fig = plt.figure(figsize=(5, 5))
ax0 = fig.add_subplot(111)
ax0.scatter(classA[0], classA[1], marker='^', c='yellow', edgecolor='black')
ax0.scatter(classB[0], classB[1], marker='o', c='blue', edgecolor='black')
ax0.scatter(classC[0], classC[1], marker='s', c='red', edgecolor='black')

# Calculate the mean vectors per class
# Creates a 2x1 vector consisting of the means of the dimensions
mean_classA = np.mean(classA, axis=1).reshape(2, 1)
mean_classB = np.mean(classB, axis=1).reshape(2, 1)
mean_classC = np.mean(classC, axis=1).reshape(2, 1)

# Calculate the scatter matrices for the SW (Scatter within) and sum the elements up
# we do not calculate the covariance matrix here

scatter_classA = np.dot((classA - mean_classA), (classA - mean_classA).T)
scatter_classB = np.dot((classB - mean_classB), (classB - mean_classB).T)
scatter_classC = np.dot((classC - mean_classC), (classC - mean_classC).T)

# Calculate the SW by adding the scatters within classes
SW = scatter_classA + scatter_classB + scatter_classC
print("Scatter Within")
print(SW)

# Calculate the scatter matrices for the SB (Scatter between) and sum the elements up
scatter_classA = np.dot(10 * (classA - mean_classA), (classA - mean_classA).T)
scatter_classB = np.dot(10 * (classB - mean_classB), (classB - mean_classB).T)
scatter_classC = np.dot(10 * (classC - mean_classC), (classC - mean_classC).T)

# Calculate the SB by adding the scatters between classes
SB = scatter_classA + scatter_classB + scatter_classC
print("Scatter Between")
print(SB)

# Compute the Eigenvalues and Eigen vectors of SW^-1 SB
eigval, eigvec = np.linalg.eig(np.dot(np.linalg.inv(SW), SB))

print(eigval)
print(eigvec)

# Select the two largest eigenvalues
eigen_pairs = [[np.abs(eigval[i]), eigvec[:, i]] for i in range(len(eigval))]
eigen_pairs = sorted(eigen_pairs, key=lambda k: k[0], reverse=True)
w = np.hstack((eigen_pairs[0][1][:, np.newaxis].real, eigen_pairs[1][1][:, np.newaxis].real))

class1 = classA.transpose()
class2 = classB.transpose()
class3 = classC.transpose()

y1 = class1.dot(w)
y2 = class2.dot(w)
y3 = class3.dot(w)

print("Final Values:")
print("Class A vector")
print(y1)
print("Class B vector")
print(y2)
print("Class C vector")
print(y3)


# Plot the data and the graph
fig = plt.figure(figsize=(5, 5))
ax0 = fig.add_subplot(111)
ax0.scatter(classA[0], classA[1], marker='^', c='yellow', edgecolor='black')
ax0.scatter(classB[0], classB[1], marker='o', c='blue', edgecolor='black')
ax0.scatter(classC[0], classC[1], marker='s', c='red', edgecolor='black')
ax0.set_xlim(0, 3)
ax0.set_ylim(0, 3)

list1, list2 = [], []
for i in range(len(y1)):
    list1.append(y1[i][0])
    list2.append(y1[i][1])

# plt.plot(list1, list2)

list1, list2 = [], []
for j in range(len(y2)):
    list1.append(y2[j][0])
    list2.append(y2[j][1])
# plt.plot(list1, list2), plt.xlabel('Range'), plt.ylabel('Range'), plt.title("Fisher's LD")

list1, list2 = [], []
for i in range(len(y3)):
    list1.append(y3[i][0])
    list2.append(y3[i][1])

# plt.plot(list1, list2)

plt.show()
