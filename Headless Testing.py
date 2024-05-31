from selenium import webdriver
import time

#For Chrome
def headless_chrome():
    driver = webdriver.Chrome()
    driver.headless = True
    time.sleep(2)
    return driver


driver = headless_chrome()
driver.get("https://www.nopcommerce.com/en/demo")
print(driver.title)
print(driver.current_url)
driver.close()