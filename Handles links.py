from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

#click on link
#driver.find_element(By.LINK_TEXT, "Digital downloads").click()
#driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()

#FIND NUMBER OF LINKS IN A PAGE
#links=driver.find_elements(By.TAG_NAME, "a")
links=driver.find_elements(By.XPATH, "//a")

print("total number of links:",len(links))

#print all the link names
for link in links:
    print(link.text)

