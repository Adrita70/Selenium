#Full xpath
#/html/body/nav/div/div[2]/div[2]/ul/li[2]/a/button

#Partial Xpath
#//*[@id="navbarSupportedContent"]/div[2]/ul/li[2]/a/button

#/html/body/div/div[1]/div/div[1]/div/div[1]/img

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.get("https://www.facebook.com/")
time.sleep(2)

#Absoulate Xpath

#driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[1]/div[1]/input").send_keys("adrita@gmail.com")
#time.sleep(2)

#Relative/Partial xpath
driver.find_element(By.XPATH,"//*[@id='email']").send_keys("adrita@gmail.com")
time.sleep(2)
