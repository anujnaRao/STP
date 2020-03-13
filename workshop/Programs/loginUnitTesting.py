from selenium import webdriver
import unittest

driver = webdriver.Chrome("G:../Drivers/x32/chromedriver.exe")
driver.get("https://gnsaddy.github.io/webAutomationSelenium/")

driver.maximize_window()

# driver.find_element_by_css_selector("input[data-testid='royal_email']")
email = driver.find_element_by_id("inputEmail")
password = driver.find_element_by_id("inputPassword")

loginBtn = driver.find_element_by_css_selector("input[type='button']")

username = "abcd"
pwd = "ab12"

email.send_keys(username)
password.send_keys(pwd)

loginBtn.click()