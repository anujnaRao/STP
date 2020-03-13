import time
import unittest
from selenium import webdriver


class Login(unittest.TestRunner):
    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://gnsaddy.github.io/webAutomationSelenium/")
        email = self.driver.find_element_by_id("inputEmail")
        password = self.driver.find_element_by_name("inputPassword")
        email.send_keys("abc@gmail.com")
        password.send_keys("1234")
        submitbtn = self.driver.find_element_by_css_selector("input[type='button']")
        submitbtn.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
