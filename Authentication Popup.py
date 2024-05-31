from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://the-internet.herokuapp.com/basic_auth")
time.sleep(5)
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")
time.sleep(5)
