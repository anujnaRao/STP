import unittest

from selenium import webdriver


class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(
            "G:\\workspace\\MCA\\4th_SEMESTER\\STP\\workshop\\Drivers\\x32\\chromedriver.exe")

    def test_search_by_text(self):
        self.driver.get("https://www.facebook.com/")
        email = self.driver.find_elements_by_name("email")
        email.clear()
        email.send_keys("anujna.p.rao@gmail.com")
        password = self.driver.find_elements_by_name("pass")
        password.clear()
        password.send_keys("07@05@1998")
        submitbtn = self.driver.find_element_by_css_selector("input[type='submit']")
        submitbtn.click()

    def tearDown(self):
        self.driver.quit()
