from selenium import webdriver
import os, time

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
driver = webdriver.Chrome(path)
driver.get("https://www.google.com/")
screenPath = os.path.join(my_path, "../ScreenPrint/")
timestr=time.strftime("%Y%m%d=%H%M%S")
driver.maximize_window()
# css
# searchBox = driver.find_element_by_css_selector("input[title='Search']")
# scB = driver.find_element_by_name("input[name='q']")
# xpath
searchB = driver.find_element_by_xpath("//input[@role='combobox']")

# from browser from inspect we can copy
searchB.send_keys("Selenium easy")
time.sleep(3)

driver.save_screenshot(screenPath + "GooglePage_"+timestr+".png")
driver.find_element_by_id("lga")
# write what you want to search inside the parentheses
magnifyingGlass = driver.find_element_by_css_selector("input[type='submit']")
magnifyingGlass.click()

# magnifyingGlass.submit()
# magnifyingGlass.send_keys("Selenium easy")

nextSearch = driver.find_element_by_xpath("//*[@id='rso']/div[1]/div/div[1]/div/div/div[1]/a/h3")
time.sleep(3)
nextSearch.click()
