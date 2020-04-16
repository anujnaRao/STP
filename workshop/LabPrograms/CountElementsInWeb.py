import unittest
import time

timestr = time.strftime("%y%m%d-%H%M%S")
from selenium import webdriver


class TestCount(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
        self.driver.get("file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/democount.html")
        self.driver.maximize_window()
        time.sleep(3)

    def test_CountElements(self):
        textboxes = self.driver.find_elements_by_id("User input")
        print("The count of TextBoxes = ", len(textboxes))

        textattr = self.driver.find_elements_by_name("abc")
        print("The count of TextBoxes using name attr = ", len(textattr))

        combobox = self.driver.find_elements_by_xpath(".//select")
        print("The count of Combo Box = ", len(combobox))

        radio = self.driver.find_elements_by_class_name("radioclass")
        print("The count of Radio Buttons = ", len(radio))

        linktext = self.driver.find_elements_by_xpath(".//a")
        print("The count of Link Texts = ", len(linktext))

        checkbox = self.driver.find_elements_by_css_selector("input[type='checkbox']")
        print("The count of Check Boxes = ", len(checkbox))

        tag = self.driver.find_elements_by_tag_name("img")
        print("The count of images = ", len(tag))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

