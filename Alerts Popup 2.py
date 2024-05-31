from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://mail.rediff.com/cgi-bin/login.cgi")

#opens alert window
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()#Sign button

alertwindow=driver.switch_to.alert
time.sleep(5)
alertwindow.accept()#close alert window by using OK button
