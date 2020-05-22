from selenium import webdriver
import os
import time

employee_source_file = "file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/LabProgramsMaterials/Emp1.html"
employee_destin_file = "file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/LabProgramsMaterials/Emp2.html"


def wait_for_user_input(driver):
    """waits for the user to enter inputchecks for user entry if user has entered it displays a message otherwise sleep for 1 sec
    """
    print("waiting for user inputs in web page..")
    while (True):
        element_value = str(driver.find_element_by_id('hiddden_element').get_attribute('value'))
        if element_value != '':
            print("User inputs are ready to be copied to one more web page.")
            return
        else:
            time.sleep(1)

li = []


def is_valid_data(class_name, value):
    """checks whether the user inputs entered in each column is valid or not for every field"""
    if class_name == 'name':
        # for name, value always should be alphabets, it may contain space.
        if value.replace(' ', '').isalpha():
            return True
        else:
            return False
    elif class_name == 'emp_id':
        # this should be always digit.
        if (value.isdigit()) and (value not in li):
            li.append(value)
            return True
        else:
            return False
    elif class_name == 'join_date':
        # this should be always in format dd-mm-yyyy, 10-06-2000, and it should be greater or equal to current date.
        try:
            from datetime import datetime
            datetime.strptime(value, '%d-%m-%Y')
            present = datetime.now()
            datetime_object = datetime.strptime(value, '%d-%m-%Y')
            if present >= datetime_object:
                return True
            else:
                return False
        except:
            print("Date should be entered in dd-mm-yyyy format")
            return False
    elif class_name == 'years_of_exp':
        # It can be float or int value.
        try:
            float(value)
            return True
        except:
            return False


if __name__ == "__main__":
    is_valid_data('name', 'hi')
    # open chrome driver
    print("Opening chrome driver")
    driver_source = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
    driver_source.maximize_window()
    driver_source.get(employee_source_file)  # load web page.
    print("Chrome driver opened.")
    time.sleep(2)
    wait_for_user_input(driver_source)
    time.sleep(2)
    timer = time.strftime("%Y%m%d = %H%M%S")
    picture = "webImages"
    driver_source.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
    time.sleep(2)

    # open 2nd chrome driver to open one more website
    driver_destin = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
    driver_destin.maximize_window()
    driver_destin.get(employee_destin_file)  # load web page.
    time.sleep(4)
    # read all contents and put it in other chrome driver.
    for each_class in ['name', 'emp_id', 'join_date', 'years_of_exp']:
        source_elements = driver_source.find_elements_by_class_name(each_class)
        dest_elements = driver_destin.find_elements_by_class_name(each_class)
        for each_element_source, each_element_dest in zip(source_elements, dest_elements):
            value = str(each_element_source.get_attribute('value'))
            if is_valid_data(each_class, value):
                each_element_dest.send_keys(value)
            else:
                print("Invalid data for column name:%s ,with value:%s" % (each_class, value))

    time.sleep(3)
    timer = time.strftime("%Y%m%d = %H%M%S")
    picture = "webImages"
    driver_source.save_screenshot("../ScreenPrint/" + picture + timer + ".png")
    time.sleep(2)
    print("Copied all the data from one web page to another.")
    # quit the driver if required.
    driver_destin.quit()
    driver_source.quit()
