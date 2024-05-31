from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#impor time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")


rome_ele=driver.find_element(By.ID, "box7")
italy_ele=driver.find_element(By.ID, "box106")

act=ActionChains(driver)
act.drag_and_drop(rome_ele,italy_ele).perform() #drag and drop operation