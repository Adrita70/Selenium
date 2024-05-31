#CTRL+A
#CTRL+C
#TAB
#CTRL+V

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys

#import time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")

input1=driver.find_element(By.XPATH,"//textarea[@id='inputText1']")

input2=driver.find_element(By.XPATH,"//textarea[@id='inputText2']")


input1.send_keys("Welcome to selenium")

act=ActionChains(driver)

#input1 ---> CTRL+A (Select the text)
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()


#input1 ---> CTRL+C (Copy the text)

act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()


#press TAB key to navigate to input 2
act.send_keys(Keys.TAB)
act.perform()

#input 2---->CTRL+V  (Paste the text)
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()




