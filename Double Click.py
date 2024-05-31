from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

driver.switch_to.frame("iframeResult") #switch Frame

field1=driver.find_element(By.XPATH, "//input[@id='field1']")
field1.click()
field1.send_keys("welcome")

button=driver.find_element(By.XPATH, "//button[normalize-space()='Copy Text']")
act=ActionChains(driver)
act.double_click(button).perform() #Double click