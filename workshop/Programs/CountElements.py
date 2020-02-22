import os, time
from selenium import webdriver

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x64/geckodriver.exe")
driver = webdriver.Firefox(executable_path=path)
driver.get("https://www.facebook.com/")
radio = driver.find_elements_by_css_selector("input[name='sex']")
count = 0
for i in radio:
    count += 1

print("The count of radio button: ", count)
driver.quit()
