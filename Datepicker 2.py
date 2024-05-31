from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
time.sleep(5)

#Date Of birth
driver.find_element(By.XPATH,"//input[@id='dob']").click() #opens datepicker
time.sleep(5)

datepicker_month=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
datepicker_month.select_by_visible_text("Feb") #month

datepicker_year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
datepicker_year.select_by_visible_text("2024") #year

#alldates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']")
#for date in alldates:
    #if date.text="25":
        #datepicker.click()
        # break()


