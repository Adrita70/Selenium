from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
#time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://testautomationpractice.blogspot.com/")

#1.Select specific checkbox
#driver.find_elements(By.XPATH,"//input[@id='monday']").click()

#2.Select all checkboxs
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))#7

#3.Select Multiple checkbox by choice
#for checkbox in checkboxes:
    #weekname=checkbox.get_attribute("id")
    #if weekname=='monday' or weekname=='sunday':
            #checkbox.click()


#4.Select last 2 checkbox
#range(5,7)->(6,7) bcz range function start with 0
#total number of elements-2=starting index
#for i in range (len(checkboxes)-2,len(checkboxes)):
    #checkboxes[i].click()


#5.Select first 2 checkbox
#for i in range (len(checkboxes)):
    #if i<2:
     #checkboxes[i].click()

#6.Clear all checkboxes
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()










