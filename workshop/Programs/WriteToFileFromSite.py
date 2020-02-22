import xlwt
import os, time
#from xlutils
from selenium import webdriver

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
driver = webdriver.Chrome(path)
driver.get("https://www.google.com/")
screenPath = os.path.join(my_path, "../ScreenPrint/")
timestr = time.strftime("%Y%m%d=%H%M%S")
driver.maximize_window()
path = os.path.join(my_path, "../TestData/TestData2.xls")
searchB = driver.find_element_by_xpath("//input[@role='combobox']")
searchB.send_keys("Selenium easy")
time.sleep(3)

driver.save_screenshot(screenPath + "GooglePage_" + timestr + ".png")
driver.find_element_by_id("lga")
magnifyingGlass = driver.find_element_by_css_selector("input[type='submit']")
magnifyingGlass.click()

nextSearch = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/a/h3")
value = nextSearch.text
# print(value)

#To write
'''
wb = xlwt.Workbook()
ws = wb.add_sheet(("Sheet1"))
ws.write(0, 0, value)
wb.save(path)
nextSearch.click()
'''

wb=copy(xlrd.open_workbook(path))
wb.get_sheet(0).write(3,3,value)
wb.save(path)

