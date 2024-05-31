from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)
# driver.find_element(By.ID, "email").send_keys("rubaba@gmail.com") #ID Locators
# time.sleep(2)
# driver.find_element(By.NAME, "password").send_keys("123456") #Name Locators
# time.sleep(2)
# driver.find_element(By.ID, "login").click()
# time.sleep(2)

# LINK_TEXTS
# driver.find_element(By.LINK_TEXT, "Community forums").click()
# driver.find_element(By.PARTIAL_LINK_TEXT, "Community").click()

# CLASS
# Sliders = driver.find_elements(By.CLASS_NAME, "menu container")
# print(len(Sliders))

# TAG
# Links = driver.find_elements(By.TAG_NAME, "a")
# print(len(Links))

driver.find_element(By.CSS_SELECTOR, "input#email").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input.inputtext").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input[data-testid=royal_email]").send_keys("abc@gmail.com")
driver.find_element(By.CSS_SELECTOR, "input.inputtext[data-testid=royal_email]").send_keys("abc@gmail.com")
time.sleep(2)

driver.close()