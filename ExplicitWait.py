from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

driver.maximize_window()
mywait=WebDriverWait(driver,10) #explicit wait declaration

driver.get("https://www.google.com/")
driver.find_element(By.NAME,'q').send_keys("Selenium")
driver.find_element(By.NAME,'q').submit()

searchlink=mywait.until(EC.presence_of_element_located((By.XPATH,"//h3[text()='Selenium']"))).click()
driver.quit()