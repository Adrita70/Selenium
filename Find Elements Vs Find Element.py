from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.maximize_window()

driver.get("https://demo.nopcommerce.com/")
#find element (Return single web element)

#1.Locator matching with single web element
#element=driver.find_element(By.XPATH, "//*[@id='small-searchterms']")
#element.send_keys("Apple Macbook")

#2.Locator matching with multiple web element
#element=driver.find_element(By.XPATH, "/html/body/div[6]/div[4]")
#print (element.text)#print link from the footer

#3.Element not available than throw NoSuch Element exeption
#login_element=driver.find_element(By.LINK_TEXT,"log")


#find elements (Return multiple web element)
#1.Locator matching with single element
#elements=driver.find_elements(By.XPATH,"//*[@id='small-searchterms']")
#print(len(elements))#1

#2.Locator matching with multiple web element
#elements=driver.find_elements(By.XPATH, "/html/body/div[6]/div[4]")
#print(len(elements))#1

#3.Element not available
elements=driver.find_elements(By.LINK_TEXT,"Log")
print("elements returned:", len(elements))




