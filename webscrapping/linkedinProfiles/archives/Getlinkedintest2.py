# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 22:05:50 2021

@author: renau
"""



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time
import pandas as pd

driver = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')
driver.get('https://www.google.com')
search = driver.find_element_by_name('q')
search.send_keys('site:linkedin.com/in/ AND "Recruiter" AND "Ho Chi Minh City, Vietnam"')
search.submit()

urls =[]

while True:
    next_page_btn =driver.find_elements_by_xpath("//a[@id='pnnext']")
    if len(next_page_btn) <1:
        print("no more pages left")
        break
    else:
        urls = driver.find_elements_by_xpath("//*[@class='iUh30']")
        urls = [url.text for url in urls]
        print(urls)
        
    time.sleep( 10 )

    element =WebDriverWait(driver,5).until(expected_conditions.element_to_be_clickable((By.ID,'pnnext')))
    driver.execute_script("return arguments[0].scrollIntoView();", element)
    element.click()

df_da=pd.DataFrame()
df_da['Url']=urls

df_da.to_csv('RecruiterHoChiMinhCity.csv',encoding='utf-8-sig')
