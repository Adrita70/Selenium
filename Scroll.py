from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://ieltsonlinetests.com/")

#1.Scroll down page till end
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels move:",value)

time.sleep(5)
#2.Scroll up to starting position
driver.execute_script("window.scrollTo(0, -document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("number of pixels move:",value)
time.sleep(5)