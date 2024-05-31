from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.nopcommerce.com/en/demo")

driver.save_screenshot("C:\\Users\\User\\PycharmProjects\\pythonProject1\\homepage.png")    #Method 1
#driver.save_screenshot(os.getcwd()+"\\homepage.png") #Method 2
#driver.get_screenshot_as_file(os.getcwd()+"\\homepage.png")  #Method 3
#driver.get_screenshot_as_png()   #Method 4
#driver.get_screenshot_as_base64() #Save in binary format
driver.quit()