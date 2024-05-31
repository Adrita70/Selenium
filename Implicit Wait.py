from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(10) #Implicit wait  #seconds

driver.get("https://www.google.com/")
driver.find_element(By.NAME,'q').send_keys("Selenium")
driver.find_element(By.NAME,'q').submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()