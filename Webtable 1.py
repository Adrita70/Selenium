from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")

#count numbers of rows and columns
noofRows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))

noofColumns=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))

print(noofRows)#7
print(noofColumns)#4


#Read Specific row and column data

data=(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]")).text #Master In Selenium
print(data)

#Read all the rows and columns data
print("printing all the rows and columns data......")

for r in range(2,noofRows+1):
    for c in range(1,noofColumns+1):
        data = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]")).text
        print(data,end='         ')
    print()


#Read Data Based on conditionsy
for r in range(2,noofRows+1):
    author = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[2]")).text
    if author=="Mukesh":
        bookName= (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[1]")).text
        price = (driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]")).text
        print(bookName,"        ",author)



driver.close()