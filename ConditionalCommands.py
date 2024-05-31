from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

#driver.get("https://demo.nopcommerce.com/")
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

#is_displayed(),is_enabled()

#searchbox=driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
#print(searchbox.is_displayed())#True
#print(searchbox.is_enabled())#True


#is_selected()
#Without Selecting the radio button
radio_male=driver.find_element(By.XPATH, "//*[@id='gender-male']")
print(radio_male.is_selected())#False

#After selecting the radio button
radio_male.click()#Select the male radio button
print(radio_male.is_selected())#True


