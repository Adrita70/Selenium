from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
#Self print msg
#text_msg=driver.find_element(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/self::a").text
#print(text_msg)

#Parent
#text_msg=driver.find_element(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/parent::td").text
#print(text_msg)

#Child
#text_msg=driver.find_element(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/child::td").text
#print(text_msg)

#Length of child
#childs=driver.find_element(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/child::td")
#print(len(childs))

#Ancestor
#text_msg=driver.find_element(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr").text
#print(text_msg) #IDBI Bank A 81.97 84.43 + 3.00

#Decendant
#descendants=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/descendant::*")
#print(len(descendants)) #7

#Following
#followings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/following::*")
#print(len(followings))#2646

#Folowing-Sibling
#followingsiblings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/following-sibling::*")
#print(len(followingsiblings))#310

#preceding
#precedings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/preceding::*")
#print(len(precedings))#842


#preceding-sibling
precedingsiblings=driver.find_elements(By.XPATH,  "//a[contains(text(),'IDBI Bank')]/ancestor::tr/preceding-sibling::*")
print(len(precedingsiblings))#82

















