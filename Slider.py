from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
#impor time
driver =webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

min_slider=driver.find_element(By.XPATH, "//span[1]")
max_slider=driver.find_element(By.XPATH, "//span[2]")
print("Print location of slider before moving....")
print(min_slider.location)  #{'x': 59, 'y': 250}
print(max_slider.location)  #{'x': 510, 'y': 250}

act=ActionChains(driver)
act.drag_and_drop_by_offset(min_slider,100,0).perform()
act.drag_and_drop_by_offset(min_slider,-39,0).perform()

print("Print location of slider After moving....")
print(min_slider.location)  #
print(max_slider.location)  #

