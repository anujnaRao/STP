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
        time.sleep(5)
        # result = self.driver.find_element_by_class_name("filterTable_no_results")
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
