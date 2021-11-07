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


browser = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')

contents = []
descriptions=[]
links =[]

#Open Html links from CSV
with open(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\outputsall.csv', encoding="utf8") as cp_csv:
    cp_url = csv.reader(cp_csv)
    next(cp_csv)
    for row in cp_url:
        links = row[7]
        contents.append(links)

#link should be something like "https://www...."
for link in contents:
    
    browser.get(link)
    
    time.sleep( 5 ) 
    try:
        description = browser.find_element_by_id("main-content").text
    except:
        description = "None"
    descriptions.append(description)
    print(description)
    

    
df_da=pd.DataFrame()
df_da['Description']=descriptions
df_da['Link']=contents
df_da.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\outputsalltestdescriptions.csv',encoding='utf-8-sig')    
    

        

    