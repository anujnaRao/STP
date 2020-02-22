from selenium import webdriver
import os

# driver = webdriver.Chrome(path)
# firefox every time path has to be set
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x64/geckodriver.exe")
driver = webdriver.Chrome(path)
driver.get("https://www.seleniumeasy.com/")
