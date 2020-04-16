from selenium import webdriver
import time

employee_source_file = "file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/Emp1.html"
employee_dest_file = "file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/Lab%20Programs%20Materials/Emp2.html"


def wait_for_user_input(driver):
    print("Waiting for the user inputs...")
    while (True):
        element_value = str(driver.find_element_by_id('hidden_element1').get_attribute('value'))
        if element_value != '':
            print("User inputs are ready to be copied to one more web page.")
            return
        else:
            time.sleep(1)

#empty list
lt = []


def is_valid_data(class_name, value):
    if class_name == 'name':
        # name, value should be alphabets, it may contain space.
        if value.replace(' ', '').isalpha():
            return True
        else:
            return False
    elif class_name == 'emp_id':
        # this should always be digit.
        if (value.isdigit()) and (value not in lt):
            lt.append(value)
            return True
        else:
            return False
    elif class_name == 'join_date':
        # Acceptable format for date is dd-mm-yyyy, 18-07-2007, it should be less than or equal to current date.
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
        # It can be float or int value
        try:
            float(value)
            return True
        except:
            return False


if __name__ == "__main__":
    is_valid_data('name', 'hi')
    print("Opening chrome driver")
    driver_source = webdriver.Chrome("../drivers/x32/chromedriver.exe")
    driver_source.maximize_window()
    driver_source.get(employee_source_file)
    print("Chrome driver opened")
    wait_for_user_input(driver_source)
    # open 2nd chrome driver to open one more website
    driver_dest = webdriver.Chrome("../Drivers/x32/chromedriver.exe")
    driver_dest.maximize_window()
    driver_dest.get(employee_dest_file)
    time.sleep(8)
    # read all contents and put it in other page
    for each_class in ['name', 'emp_id', 'join_date', 'years_of_exp']:
        source_elements = driver_source.find_elements_by_class_name(each_class)
        dest_elements = driver_dest.find_elements_by_class_name(each_class)
        for each_element_source, each_element_dest in zip(source_elements, dest_elements):
            value = str(each_element_source.get_attribute('value'))
            if is_valid_data(each_class, value):
                each_element_dest.send_keys(value)
            else:
                print("Invalid data for column name:%s ,with value:%s" % (each_class, value))
    time.sleep(5)
    print("Copied all the data from one web page to other!")
    driver_dest.quit()
    driver_source.quit()