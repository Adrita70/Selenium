from selenium import webdriver

import time
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://www.nopcommerce.com/en/demo")

#capture cookies from the browser
cookies=driver.get_cookies()
print("Size of cookies:",len(cookies)) # 4


#print details of all Cookies
#for c in cookies:
    #print(c)
    #print(c.get('name'),":",c.get('value'))


#Add new cookie to the browser
driver.add_cookie({"name":"My Cookie", "value":"1234"})
cookies=driver.get_cookies()
print("Size of cookies after adding new one:",len(cookies))

#Delete specific cookie from the browser
driver.delete_cookie("My Cookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted one:",len(cookies))


#Delete all the cookies
driver.delete_cookie("My Cookie")
cookies=driver.get_cookies()
print("Size of cookies after deleted all:",len(cookies))

driver.quit()