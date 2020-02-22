import os, time
from selenium import webdriver
import unittest

my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "../Drivers/x32/chromedriver.exe")


# Unit Testing
# Test Case, Test loader, Test runner, Test Suite, Test Report
class ChromeLaunch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(path)
        driver = self.driver
        time.sleep(2)
        driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("http://www.google.com")
        textBox = self.driver.find_element_by_name('q')
        textBox.send_keys("Hello Moto")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
