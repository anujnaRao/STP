import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
np.random.seed(seed=42)

# Create data
triangles = np.array([[1, 1, 1, 2, 2, 2, 2, 2.5, 3.5, 3.5],
                      [1, 2, 3, 1, 2, 3, 3.5, 2, 1, 2]])
circles = np.array([[3.5, 3.5, 4.5, 4.5, 4.5, 5, 5, 6, 6, 6], [3, 4, 1, 2, 3, 4, 5, 3, 4, 5]])

# Plot the data
fig = plt.figure(figsize=(10, 10))
ax0 = fig.add_subplot(111)
ax0.scatter(triangles[0], triangles[1], marker='^', c='yellow', edgecolor='black')
ax0.scatter(circles[0], circles[1], marker='o', c='blue', edgecolor='black')

# Calculate the mean vectors per class
# Creates a 2x1 vector consisting of the means of the dimensions
mean_triangles = np.mean(triangles, axis=1).reshape(2, 1)
mean_circles = np.mean(circles, axis=1).reshape(2, 1)

# Calculate the scatter matrices for the SW (Scatter within) and sum the elements up

# Mind that we do not calculate the covariance matrix here because then we have to divide by n or n-1 as shown below

scatter_triangles = np.dot((triangles - mean_triangles), (triangles - mean_triangles).T)
scatter_circles = np.dot((circles - mean_circles), (circles - mean_circles).T)

# Calculate the SW by adding the scatters within classes
SW = scatter_triangles + scatter_circles
print("Scatter Within")
print(SW)

scatter_triangles = np.dot(10 * (triangles - mean_triangles), (triangles - mean_triangles).T)
scatter_circles = np.dot(10 * (circles - mean_circles), (circles - mean_circles).T)

# Calculate the SB by adding the scatters between classes
SB = scatter_triangles + scatter_circles
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

class1 = triangles.transpose()
class2 = circles.transpose()

y1 = class1.dot(w)
y2 = class2.dot(w)

print("Final Values: ")
print("Class 1 vector")
print(y1)
print("Class 2 vector")
print("\n", y2)

fig = plt.figure(figsize=(10, 10))
ax0 = fig.add_subplot(111)
ax0.scatter(triangles[0], triangles[1], marker='^', c='yellow', edgecolor='black')
ax0.scatter(circles[0], circles[1], marker='o', c='blue', edgecolor='black')
ax0.set_xlim(-1, 10)
ax0.set_ylim(-1, 10)

list1, list2 = [], []

for i in range(10):
    list1.append(y1[i][0])
    list2.append(y1[i][1])

plt.plot(list1, list2)

list1, list2 = [], []
for j in range(10):
    list1.append(y2[j][0])
    list2.append(y2[j][1])
plt.plot(list1,list2)

plt.show()
