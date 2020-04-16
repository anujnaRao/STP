import unittest
import time
from selenium import webdriver


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/loginPage.html")
        email = self.driver.find_element_by_xpath('//*[@id="User"]')
        password = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        email.send_keys("admin")
        password.send_keys("root123")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        submitbtn.click()
        time.sleep(5)
        print("Valid Email and Password")
        # alertJS = self.driver.switch_to.alert
        # print(alertJS.text)
        # alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../ScreenPrint/" + picture + timeer + ".png")
        time.sleep(5)

    def test_chrome_fn1(self):
        self.driver.get("file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/loginPage.html")
        email = self.driver.find_element_by_xpath('//*[@id="User"]')
        password = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        email.send_keys("xyz")
        password.send_keys("root123")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        submitbtn.click()
        time.sleep(5)
        print("Invalid Email with valid Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../ScreenPrint/" + picture + timeer + ".png")
        time.sleep(5)

    def test_chrome_fn2(self):
        self.driver.get("file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/loginPage.html")
        email = self.driver.find_element_by_xpath('//*[@id="User"]')
        password = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        email.send_keys("admin")
        password.send_keys("123")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        submitbtn.click()
        time.sleep(5)
        print("Valid Email with invalid Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../ScreenPrint/" + picture + timeer + ".png")
        time.sleep(5)

    def test_chrome_fn3(self):
        self.driver.get("file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/loginPage.html")
        email = self.driver.find_element_by_xpath('//*[@id="User"]')
        password = self.driver.find_element_by_xpath('//*[@id="Pass"]')
        email.send_keys("abc@gmail.com")
        password.send_keys("xyz")
        submitbtn = self.driver.find_element_by_xpath('//*[@id="btn"]')
        submitbtn.click()
        time.sleep(5)
        print("Invalid Email and Password")
        alertJS = self.driver.switch_to.alert
        print(alertJS.text)
        alertJS.accept()
        timeer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../ScreenPrint/" + picture + timeer + ".png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
