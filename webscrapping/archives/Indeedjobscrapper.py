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



#specify driver path and login

DRIVER_PATH = './chromedriver.exe'
####DDRIVER_PATH = '/usr/local/bin/chromedriver'

driver = webdriver.Chrome(executable_path = DRIVER_PATH)
driver.implicitly_wait(3)

driver.get('https://ca.indeed.com/')

"""
name = driver.find_element_by_xpath('//input[@id="login-email-input"]')
name.send_keys(['xxx'])

password = driver.find_element_by_xpath('//input[@id="login-password-input"]')
password.send_keys(['xxxx'])
"""
#accept cookies
try:
    cookie = driver.find_element_by_xpath("//button[contains(text(),'OK')]")
    cookie.click()
except:
    pass


#search job type
jobtype = driver.find_element_by_xpath('//input[@id="text-input-what"]')
jobtype.send_keys(['data science'])

#search location
location = driver.find_element_by_xpath('//input[@id="text-input-where"]')
location.send_keys(['Quebec'])


#click search
find = driver.find_element_by_xpath("//button[contains(text(),'Find jobs')]")
find.click()

################## advance search
advanced_search = driver.find_element_by_xpath("//a[contains(text(),'Advanced Job Search')]")
advanced_search.click()

#search data science 


search_button = driver.find_element_by_xpath('//*[@id="fj"]')
search_button.click()

close_popup = driver.find_element_by_id("popover-x")
close_popup.click()



"""
This code helps you get relevant information from each job card, and then iterate through all job cards on one page.
Then go to the next page
"""
"""
#let the driver wait 3 seconds to locate the element before exiting out
driver.implicitly_wait(3) 

titles=[]
companies=[]
locations=[]
links =[]
reviews=[]
salaries = []


#Bug loop
for i in range(0,3):
    
  
   
  #job_card = driver.find_elements_by_xpath('//div[contains(@class,"job_seen_beacon")]')
  job_card = driver.find_elements_by_xpath('//a[contains(@id,"job_")]')
    
  for job in job_card:
       
    #.  not all companies have review
        try:
            review = job.find_element_by_xpath('.//span[@class="ratingNumber"]').text
        except:
            review = "None"
        reviews.append(review)


        try:
            location = job.find_element_by_xpath('.//div[contains(@class,"companyLocation")]').text
        except:
            location = "None"
    #.  tells only to look at the element       
        locations.append(location)
        

  
        try:
            title  = job.find_element_by_xpath('.//h2[@class="jobTitle jobTitle-color-purple"]//span').text
        except:
            title = job.find_element_by_xpath('.//h2[@class="jobTitle jobTitle-color-purple"]//span').get_attribute(name="title")
        titles.append(title)
        print(title)
        
        #links.extend([x.get_attribute("href") for x in job.find_elements_by_xpath('.//a[contains(@id, "job_")]')])
        #####links.append(job.find_element_by_xpath('.//a[contains(@id, "job_")]').get_attribute(name="href"))
        links.append(job.get_attribute(name="href"))
        
        companies.append(job.find_element_by_xpath('.//span[@class="companyName"]').text)

 

if 1 == 2:    
    try:
           next_page = driver.find_element_by_xpath('//a[@aria-label={}]//span[@class="pn"]'.format(i+2))
           next_page.click()
                

            
    
    except:
           next_page = driver.find_element_by_xpath('//a[@aria-label="Next"]//span[@class="np"]')
           next_page.click()
            #except:
                #next_page = driver.find_element_by_xpath('//a[.//span[contains(text(),"Next")]]')
                #next_page.click()
                

    print("Page: {}".format(str(i+2)))           


descriptions=[]
for link in links:
    
    driver.get(link)
    jd =  driver.find_element_by_xpath('//div[@id="jobDescriptionText"]').text
    descriptions.append(jd)




df_da=pd.DataFrame()
df_da['Title']=titles
df_da['Company']=companies
df_da['Location']=locations
df_da['Link']=links
df_da['Review']=reviews
 
    
        

df_da.to_excel('indeedresults.xlsx', index = False)


"""






