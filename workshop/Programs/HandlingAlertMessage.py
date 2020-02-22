import os, time
from selenium import webdriver

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")
driver = webdriver.Chrome(path)
driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
clickBtn = driver.find_element_by_css_selector("button[onclick='myAlertFunction\(\)']")
clickBtn.click()

time.sleep(5)
alertj = driver.switch_to.alert
print(alertj.text)
#okay
alertj.accept()
#cancel
#alertj.dismiss()