#import requests as requests
#from selenium import webdriver
#from selenium.webdriver.common.by import By

#driver = webdriver.Chrome()
#driver.maximize_window()
#driver.implicitly_wait(10)
#driver.get("http://www.deadlinkcity.com/")

#alllinks=driver.find_elements(By.TAG_NAME,'a')
#count=0

#for link in alllinks:
    #url=link.get_attribute('href')
  #try:
   # res=requests.head(url)
   #except:
   # if res.status_code>=400:
        #print(url, "in broken link")
       # count+=1

    #else:
        #print(url, "in valid link")
#print ("total number of broken links:",count)




