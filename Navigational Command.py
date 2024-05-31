from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.maximize_window()

driver.get("https://www.amazon.com/")
driver.get("https://www.daraz.com.bd/")
#driver.back()#amazon
driver.forward()#daraz
driver.refresh()
driver.quit()
