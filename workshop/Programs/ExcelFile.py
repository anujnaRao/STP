import os
import xlrd
from selenium import webdriver

my_path=os.path.abspath(os.path.dirname(__file__))
driverpath = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
path =os.path.join(my_path,"../TestData/TestData.xls")
driver = webdriver.Chrome(driverpath)
driver.maximize_window()
