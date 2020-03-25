import time
import unittest
from selenium import webdriver


class Table_Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    def test_chrome_fn(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("Software")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search2 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input')
        search2.send_keys("6")
        search3 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        search3.send_keys("UsernameName")
        search4 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
        search4.send_keys("First name")
        search5 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
        search5.send_keys("Last Name")
        print("Result not Found")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
