from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.opencart.com/index.php?route=account/register")
drpcountry=driver.find_element(By.XPATH, "//select[@id='input-country']")
#drpcountry=Select(driver.find_element(By.XPATH, "//select[@id='input-country']"))

#Select option for the dropdown

#drpcountry.select_by_visible_text("India")
#drpcountry.select_by_value("10")#Argentina
#drpcountry.select_by_index(13) # index

