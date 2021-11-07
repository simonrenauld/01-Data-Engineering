

# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:05:50 2021

@author: renau
"""

import urllib
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
driver = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')  


root = "https://www.google.com/"
url = "https://google.com/search?q="
query = 'site:linkedin.com/in/ AND "Technical Recruiter" AND "Ho Chi Minh City, Vietnam"'  # Fill in google query
query = urllib.parse.quote_plus(query)
link = url + query
links =[]

counter = 0


print(f'Main link to search for: {link}')

options = Options()
# options.headless = True
options.add_argument("--window-size=1920,1200")

driver.get(link)

wait = WebDriverWait(driver, 15)
wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class = "g"]')))

for i in range(counter,10):
    page_no = driver.find_elements_by_xpath("//table[@class='AaVjTc']/tbody/tr/td/a")
    page_no[i].click()
    
    time.sleep( 30 )

    value = driver.find_elements_by_xpath('//div[@class="r"]/a')
    headings = driver.find_elements_by_xpath('//div[@class = "g"]')  
    for heading in headings:
        title = heading.find_elements_by_tag_name('h3')
        link = heading.find_element_by_css_selector('.yuRUbf>a').get_attribute("href")  
        links.append(link)    

df_da=pd.DataFrame()
df_da['Title']=links

df_da.to_csv('.\outputs\RecruiterdatascienceHoChiMinhCity.csv',encoding='utf-8-sig')
