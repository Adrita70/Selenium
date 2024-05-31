from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0) #Switch to frame
time.sleep(5)

#mm/dd/yy
#driver.find_element(By.XPATH, "//input[@id='datepicker']").send_keys("02/23/2024")
#time.sleep(5)

year="2024"
month="February"
date="2/23/2024"
driver.find_element(By.XPATH, "//input[@id='datepicker']").click() #opens datepicker
time.sleep(5)

while True:
    mon=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text

    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[2]/span").click() #next arrow
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  # previous arrow
#Select date
