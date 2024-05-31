from selenium import webdriver

ops= webdriver.ChromeOptions()#notification popup
ops.add_argument('--disable-notification')#notification popup

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://whatmylocation.com/")


