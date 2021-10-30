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


browser = webdriver.Chrome(executable_path=r'./chromedriver')

contents = []
descriptions=[]

#Open Html links from CSV
with open('indeedresults.csv', 'rt') as cp_csv:
    cp_url = csv.reader(cp_csv)
    next(cp_csv)
    for row in cp_url:
        links = row[4]
        contents.append(links)

#link should be something like "https://www...."
for link in contents:
    
    browser.get(link)
    
    
    try:
        description = link.find_element_by_class_name("jobDescriptionText").text
    except:
        description = "None"
        descriptions.append(description)
        print(description)
    
    time.sleep( 5 )
    

        

    
