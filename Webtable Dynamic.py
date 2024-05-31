from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login
driver.find_element(By.Id,"txtUsername").send_keys("Admin")
driver.find_element(By.Id,"txtPassword").send_keys("admin123")
driver.find_element(By.Id,"btnLogin").click()

#Admin->User Management ->Users
driver.find_element(By.XPATH," ").click()
driver.find_element(By.XPATH," ").click()
driver.find_element(By.Xpath," ").click()

#total rows and a table
rows=len(driver.find_elements(By.XPATH," "))
print(rows)

count=0
for r in range(1,rows+1):
    status=driver.find_elements(By.XPATH,"").text
    #if status=="Enabled"
      #  count=count+1
