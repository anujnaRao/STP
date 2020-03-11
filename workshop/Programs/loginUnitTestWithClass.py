import time
import unittest

from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')

    def test_search_by_text(self):
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_element_by_name("email")
        email.clear()
        email.send_keys("anujna.p.rao@gmail.com")
        password = self.driver.find_element_by_name("pass")
        password.clear()
        password.send_keys("07@05@1998")
        submitbtn = self.driver.find_element_by_css_selector("input[type='submit']")
        submitbtn.click()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
