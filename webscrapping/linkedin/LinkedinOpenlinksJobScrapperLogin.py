# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 14:21:52 2021

@author: Simon Renauld
"""
import csv
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as browser_wait
from selenium.webdriver.support import expected_conditions as EC
import requests
import time
import pandas as pd
import re


browser = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')

contents = []
descriptions=[]
links =[]


#Open Html links from CSV
with open(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\Results\outputsallVietnam.csv', encoding="utf8") as cp_csv:
    cp_url = csv.reader(cp_csv)
    next(cp_csv)
    for row in cp_url:
        links = row[6]
        contents.append(links)
        
        
 # driver.get method() will navigate to a page given by the URL address
browser.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

time.sleep( 1 ) 

# locate email form by_class_name
username = browser.find_element_by_xpath('//input[@id="username"]')
username.send_keys('testemai378@gmail.com')

username = browser.find_element_by_xpath('//input[@id="password"]')
username.send_keys('testemai378123')

#click login
find = browser.find_element_by_xpath("//button[contains(text(),'Sign in')]")
find.click()
       
time.sleep( 1 ) 

#link should be something like "https://www...."
for link in contents:
    
    browser.get(link) 
    

    
    try:
        cookie = browser.find_element_by_xpath('/html/body/div[7]/div[3]/div/div[1]/div[1]/div/div[2]/footer/button').click()
        cookie.click()
        
    except:
        pass
    
    time.sleep( 3 ) 
    try:
        description = browser.find_element_by_id("job-details").text # adapt to your html page
    except:
        description = "None"
    descriptions.append(description)
    


    
 
df_da=pd.DataFrame()
df_da['Description']=descriptions
df_da['Link']=contents

# Delete all text after string    
df_da['Description'] = df_da['Description'].str.split('Similar jobs').str[0]
df_da['Description'] = df_da['Description'].str.split('Off').str[0]
df_da.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\Results\outputsalldescriptionsVietnam.csv',encoding='utf-8-sig')    
    

        

    
