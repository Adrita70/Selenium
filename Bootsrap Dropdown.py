from selenium import webdriver
from selenium.webdriver.common.by import By


#import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.find_elements(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countrilist=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")

print(len(countrilist))

for country in countrilist:
    if country.text== "United Kingdom":
        country.click()
        break
