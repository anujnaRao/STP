import time
import unittest
from selenium import webdriver


class TableValueValid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    def test_validate_fn1(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("Nora Smith")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search2 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input')
        search2.send_keys("Bill")
        time.sleep(2)
        print("Invalid value for table one and invalid value for table two")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn2(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("deployed")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search2 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input')
        search2.send_keys("Jennifer")
        time.sleep(2)
        print("Valid value for table one and invalid value for table two")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn3(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("8")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search3 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        search3.send_keys("larrypt")
        time.sleep(2)
        print("Invalid value for table one and valid value for table two ")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn4(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("4")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search2 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[1]/input')
        search2.send_keys("1")
        # search3 = self.driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        # search3.send_keys("jacobs")
        # search4 = self.driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
        # search4.send_keys("Brigade")
        # search5 = self.driver.find_element_by_xpath(
        #     '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
        # search5.send_keys("Kathaniko")
        print("Valid value for both the Tables - # values")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn5(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("Wireframes")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search3 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[2]/input')
        search3.send_keys("jacobs")
        print("Valid value for both the Tables - Task and username values")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn6(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("Emily John")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search3 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[3]/input')
        search3.send_keys("Byron")
        print("Valid value for both the Tables - Assignee and First Name values")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def test_validate_fn7(self):
        self.driver.get("https://www.seleniumeasy.com/test/table-search-filter-demo.html")
        search = self.driver.find_element_by_xpath('//*[@id="task-table-filter"]')
        search.send_keys("completed")
        time.sleep(2)
        filterButton = self.driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/div/div/div/button')
        filterButton.click()
        search3 = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/div[2]/div[2]/div/table/thead/tr/th[4]/input')
        search3.send_keys("Swarroon")
        print("Valid value for both the Tables - Status and Last Name values")
        timer = time.strftime("%Y%m%d = %H%M%S")
        picture = "webImages"
        # taking screenshots
        # self.driver.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
