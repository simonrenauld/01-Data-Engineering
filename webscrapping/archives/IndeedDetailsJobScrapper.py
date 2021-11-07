# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 13:38:01 2021

@author: renau
"""

#let the driver wait 3 seconds to locate the element before exiting out
driver.implicitly_wait(3) 

titles=[]
companies=[]
locations=[]
links =[]
reviews=[]
salaries = []
descriptions=[]


for i in range(0,20):
    
    job_card = driver.find_elements_by_xpath('//div[contains(@class,"clickcard")]')
    
    for job in job_card:
       
    #.  not all companies have review
        try:
            review = job.find_element_by_xpath('.//span[@class="ratingsContent"]').text
        except:
            review = "None"
        reviews.append(review)
   #.   not all positions have salary
        try:
            salary = job.find_element_by_xpath('.//span[@class="salaryText"]').text
        except:
            salary = "None"
    #.  tells only to look at the element       
        salaries.append(salary)
        
        try:
            location = job.find_element_by_xpath('.//span[contains(@class,"location")]').text
        except:
            location = "None"
    #.  tells only to look at the element       
        locations.append(location)
        
        try:
            title  = job.find_element_by_xpath('.//h2[@class="title"]//a').text
        except:
            title = job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="title")
        titles.append(title)
        links.append(job.find_element_by_xpath('.//h2[@class="title"]//a').get_attribute(name="href"))
        companies.append(job.find_element_by_xpath('.//span[@class="company"]').text)
        
    
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