from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/en/orangehrm-starter-open-source-software/")

windowid=driver.current_window_handle
print ("window id",windowid) #window id 66CC600AE34351EDFCCBA03E873CD473