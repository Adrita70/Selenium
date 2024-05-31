from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

#opens alert window
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()

alertwindow=driver.switch_to.alert

print(alertwindow.text)
alertwindow.send_keys("WELCOME")
time.sleep(5)

#alertwindow.accept()#close alert window by using OK button
alertwindow.dismiss()#close alert window by using CANVCEL button