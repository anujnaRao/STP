import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains


class TableValueValid(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome('../Drivers/x32/chromedriver.exe')
        time.sleep(2)
        self.driver.maximize_window()

    def test_validate_fn1(self):
        self.driver.get("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
        time.sleep(2)

        #For first Span
        dragSpan1 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[1]')
        # dragSpan = self.driver.find_element_by_css_selector("span[draggable='true']")
        time.sleep(2)
        print('Dragging the element')
        droppable = self.driver.find_element_by_id("mydropzone")
        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop(dragSpan1, droppable).perform()
        self.assertEqual("Dropped!", droppable.text)

        # For Second Span
        dragSpan2 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[2]')
        # dragSpan = self.driver.find_element_by_css_selector("span[draggable='true']")
        time.sleep(2)
        print('Dragging the element')
        droppable = self.driver.find_element_by_id("mydropzone")

        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop(dragSpan2, droppable).perform()

        # For Third Span
        dragSpan3 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[3]')
        # dragSpan = self.driver.find_element_by_css_selector("span[draggable='true']")
        time.sleep(2)
        print('Dragging the element')
        droppable = self.driver.find_element_by_id("mydropzone")

        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop(dragSpan3, droppable).perform()

        # For Fourth Span
        dragSpan4 = self.driver.find_element_by_xpath('//*[@id="todrag"]/span[4]')
        # dragSpan = self.driver.find_element_by_css_selector("span[draggable='true']")
        time.sleep(2)
        print('Dragging the element')
        droppable = self.driver.find_element_by_id("mydropzone")

        actionChains = ActionChains(self.driver)
        actionChains.drag_and_drop(dragSpan4, droppable).perform()

        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
