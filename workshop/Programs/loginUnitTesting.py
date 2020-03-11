from selenium import webdriver

driver = webdriver.Chrome("G:\\workspace\\MCA\\4th_SEMESTER\\STP\\workshop\\Drivers\\x32\\chromedriver.exe")
driver.get("https://www.facebook.com/")

driver.maximize_window()

# driver.find_element_by_css_selector("input[data-testid='royal_email']")
email = driver.find_elements_by_id("email")
password = driver.find_elements_by_id("pass")

loginBtn = driver.find_element_by_css_selector("input[type='submit']")

username = "abcd"
pwd = "ab12"

email.send_keys(username)
password.send_keys(pwd)

loginBtn.click()