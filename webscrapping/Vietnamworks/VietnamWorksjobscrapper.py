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

driver.get("https://www.vietnamworks.com/job-search/all-jobs?filtered=true")
wait=WebDriverWait(driver, 10)

titles=[]
links =[]

time.sleep( 5 )

###########################################################################################
# Click search Button 
try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "button searchBar__button")]'))).click()
except:
    pass

try:
    wait.until(EC.element_to_be_clickable((By.XPATH, '//a[contains(@class, "button searchBar__button")]'))).click()
except:
    pass

###########################################################################################
#loop

for i in range(0,180):
    
    job_card = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[contains(@class,'job-info-wrapper ')]//a[@class='job-title priorityJob']")))
    print(len(job_card))
    for job in job_card:
        links.append(job.get_attribute("href"))
        titles.append(job.text)
        print(job.get_attribute("href"),job.text)

    try:
        wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='page-link' and .='>']"))).click()      
    except NoSuchElementException:
        break


print("Page: {}".format(str(i+2)))           
    
df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Link']=links
    
        
print(df_da)
    
        

df_da.to_csv('.\outputs\jobvietnamwork11122021_v3test.csv',encoding='utf-8-sig')



