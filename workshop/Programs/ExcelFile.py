import os, time
import xlrd
from selenium import webdriver

my_path = os.path.abspath(os.path.dirname(__file__))
driverpath = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
path = os.path.join(my_path, "../TestData/TestData.xls")
timestr=time.strftime("%Y%m%d=%H%M%S")
driver = webdriver.Chrome(driverpath)
driver.maximize_window()

time.sleep(3)
driver.get("https://facebook.com")
time.sleep(3)
email = driver.find_element_by_id("email")
password = driver.find_element_by_id("pass")
loginBtn = driver.find_element_by_css_selector("input[type='submit']")

book = xlrd.open_workbook(path)

ws = book.sheet_by_index(0)
username = ws.cell_value(1, 0)
pwd = ws.cell_value(1, 1)

email.send_keys(username)
password.send_keys(str(pwd))
time.sleep(2)

screenPath = os.path.join(my_path, "../ScreenPrint/")
driver.save_screenshot(screenPath + "GooglePage_"+timestr+".png")
loginBtn.click()