from collections import OrderedDict
from xlutils.copy import copy
from selenium import webdriver
import xlrd
import time

# excel_fname = "../marksfortesting.xls"
excel_fname = "../LabProgramsMaterials/marks.xls"
student_page = "file:///G:/workspace/MCA/4th_SEMESTER/STP/workshop/LabProgramsMaterials/student.html "


def read_from_excel(path):
    book = xlrd.open_workbook(path)
    # Select First sheet of workbook
    firstSheet = book.sheet_by_index(0)
    mdict = OrderedDict()
    for each_name, index in zip(firstSheet.col_values(0, 1), range(1, firstSheet.row_len(0))):
        eachrow = firstSheet.row_values(index, 1)
        mdict[str(each_name)] = eachrow
    return mdict


def calculate_result(driver, mdict):
    number_of_subjects = 5
    student_name_objects = driver.find_elements_by_xpath("//*[@id='student_name']")
    marks_objects = driver.find_elements_by_class_name("marks")
    for (each_item_key, values), index in zip(mdict.items(), range(0, number_of_subjects)):
        student_name_objects[index].send_keys(each_item_key)
        for each_marks, index_value in zip(values, range(0, len(values))):
            marks_objects[0].send_keys(str(each_marks))
            del marks_objects[0]
    time.sleep(3)
    driver.find_element_by_id("calculate").click()
    print("Clicked on calculate!")


def get_total_percentage_result(driver):
    time.sleep(5)
    total_objects = driver.find_elements_by_class_name("total")
    percentage_objects = driver.find_elements_by_class_name("percentage")
    result_objects = driver.find_elements_by_class_name("result")
    total = []
    percent = []
    result = []
    for each_total_obj in total_objects:
        total.append(str(each_total_obj.get_attribute('value')))
    for each_percentage_obj in percentage_objects:
        percent.append(str(each_percentage_obj.get_attribute('value')))
    for each_result_obj in result_objects:
        result.append(str(each_result_obj.get_attribute('value')))
    print("Total:" + str(total))
    print("Percentage:" + str(percent))
    print("Result:" + str(result))
    return total, percent, result


def append_to_excel(calculated_results):
    # Appends total, percentage, result to new excel sheet called marks.
    number_of_subjects = 5
    total, percent, result = calculated_results
    rb = xlrd.open_workbook("marks.xls")
    r_sheet = rb.sheet_by_index(0)
    c = r_sheet.ncols  # total number of columns
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(0, c, "Total")  # Append the column 'Total' at the end in excel sheet
    for each_total_value, index in zip(total, range(1, number_of_subjects + 1)):
        sheet.write(index, c, each_total_value)
    sheet.write(0, c + 1, "Percentage")  # Append the column 'Percentage' at the end in excel sheet
    for each_percent_value, index in zip(percent, range(1, number_of_subjects + 1)):
        sheet.write(index, c + 1, each_percent_value)
    sheet.write(0, c + 2, "Result")  # Append the column 'Result' at the end in excel sheet
    for each_result_value, index in zip(result, range(1, number_of_subjects + 1)):
        sheet.write(index, c + 2, each_result_value)
    wb.save(excel_fname)
    print('Excel sheet was saved successfully!')


if __name__ == '__main__':
    '''Read excel sheet,show it on page, calculate the results,read calculated results through selenium and append 
    the result in excel sheet '''
    mdict = read_from_excel(excel_fname)
    print(mdict)

driver = webdriver.Chrome("../drivers/x32/chromedriver.exe")

path = student_page
driver.get(path)
time.sleep(4)
driver.maximize_window()
calculate_result(driver, mdict)

calculation_results = get_total_percentage_result(driver)

append_to_excel(calculation_results)
print("Browser is closed!")
driver.quit()