from selenium import webdriver
import os

# driver = webdriver.Chrome(path)
# firefox every time path has to be set
my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
driver = webdriver.Chrome(path)

# Have to give absolute path of the chrome driver
driver = webdriver.Chrome("G:\\workspace\\MCA\\4th_SEMESTER\\STP\\workshop\\Drivers\\x32\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/")
