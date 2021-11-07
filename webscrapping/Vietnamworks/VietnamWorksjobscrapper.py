# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:07:08 2021
https://towardsdatascience.com/web-scraping-job-postings-from-indeed-com-using-selenium-5ae58d155daf
@author: renau
"""
import pandas as pd
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
##########################################################
#specify driver path and login
##########################################################
DRIVER_PATH = 'C:/Users/bin/chromedriver'
####DDRIVER_PATH = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.implicitly_wait(3)

driver.get('https://www.vietnamworks.com/data+in-ho-chi-minh-v29-en?filtered=true')

titles=[]
links =[]

time.sleep( 5 )

###########################################################################################
# Click search Button 
try:
    cookie = driver.find_element_by_xpath('.//a[contains(@class, "button searchBar__button")]')
    cookie.click()
except:
    pass


try:
    cookie = driver.find_element_by_xpath('.//a[contains(@class, "button searchBar__button")]')
    cookie.click()
except:
    pass
time.sleep( 5 )
###########################################################################################
#loop
for i in range(0,20):
    
  
   
  #job_card = driver.find_elements_by_xpath('//div[contains(@class,"job_seen_beacon")]')
    job_card = driver.find_elements_by_xpath('.//h3[contains(@class, "title")]')

    
    for job in job_card:
       

                                             
        try:
            title = job.find_elements_by_xpath('.//h3[contains(@class, "title")]')
        except:
            title = job.find_elements_by_xpath('.//h3[contains(@class, "title")]').get_attribute(name="title")
        titles.append(title)
        print(title)
        
        links.append(job.get_attribute(name="href"))
    
  
    time.sleep( 2 )
      

    try:
        next_page = driver.find_element_by_xpath('//li[@page-item={}]//a[@class=">"]'.format(i+2))
        next_page.click()
        
    except NoSuchElementException:
       break


print("Page: {}".format(str(i+2)))           
    
df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Title']=links
    
        

df_da.to_csv('.\outputs\gis10312021.csv',encoding='utf-8-sig')



