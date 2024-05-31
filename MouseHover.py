from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

#Login
driver.find_element(By.Id,"txtUsername").send_keys("Admin")
driver.find_element(By.Id,"txtPassword").send_keys("admin123")
driver.find_element(By.Id,"btnLogin").click()

#Admin->User Management ->Users
admin=driver.find_element(By.XPATH," ")
userman=driver.find_element(By.XPATH," ")
users=driver.find_element(By.Xpath," ")

#mouseHover
act=ActionChains()
act.move_to_element(admin).move_to_element(userman).move_to_element(users).click().perform()