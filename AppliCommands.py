from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title)#OrangeHRM
print(driver.current_url)#https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)
driver.quit()
