from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
driver.find_element(By.LINK_TEXT, "nopCommerce").click()
time.sleep(5)
driver.close()
#driver.quit()
