# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 16:59:29 2021

@author: Simon Renauld
"""

"""
Download 
https://chromedriver.chromium.org/downloads

"""


from selenium import webdriver
import time
import pandas as pd


url = 'https://www.linkedin.com/jobs/search/?geoId=100025096&keywords=data%20scientist%20french&location=Toronto%2C%20Ontario%2C%20Canada'

wd = webdriver.Chrome(executable_path='./chromedriver.exe')
wd.get(url)


"""
Get Number of jobs per link search and location
"""




"""
Get first element seen of the job
"""
job_id= []
job_title = []
company_name = []
location = []
date = []
job_link = []
for job in jobs:
 job_id0 = job.get_attribute('data-id')
 job_id.append(job_id0)
 
 job_title0 = job.find_element_by_css_selector('h3').get_attribute('innerText')
 job_title.append(job_title0)
 
 company_name0 = job.find_element_by_css_selector('h4').get_attribute('innerText')
 company_name.append(company_name0)
 
 location0 = job.find_element_by_css_selector('[class="job-result-card__location"]').get_attribute('innerText')
 location.append(location0)
 
 date0 = job.find_element_by_css_selector('div>div>time').get_attribute('datetime')
 date.append(date0)
 
 job_link0 = job.find_element_by_css_selector('a').get_attribute('href')
 job_link.append(job_link0)
