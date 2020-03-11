import os, time
from selenium import webdriver
import unittest

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x64/geckodriver.exe")


# Unit Testing
# Test Case, Test loader, Test runner, Test Suite, Test Report
class FirefoxLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox(executable_path=path)
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_firefox_fn(self):
        self.driver.get("http://www.google.com")
        textbox = self.driver.find_element_by_name('q')
        textbox.send_keys("Hello Moto")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
