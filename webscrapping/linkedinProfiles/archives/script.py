from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.element import Tag
from time import sleep
import csv
from parsel import Selector
import parameters
import numpy


# Reference 
# Function call extracting title and linkedin profile iteratively
def find_profiles():
    for r in result_div:
        # Checks if each element is present, else, raise exception
        try:
            link = r.find('a', href=True)
            title = None
            title = r.find('h3')
            
            # returns True if a specified object is of a specified type; Tag in this instance 
            if isinstance(title,Tag):
                title = title.get_text()
    
            description = None
            description = r.find('span', attrs={'class': 'st'})
    
            if isinstance(description, Tag):
                description = description.get_text()
    
            # Check to make sure everything is present before appending
            if link != '' and title != '' and description != '':
                links.append(link['href'])
                titles.append(title)
                descriptions.append(description)
            
    
        # Next loop if one element is not present
        except Exception as e:
            print(e)
            continue
        
# This function iteratively clicks on the "Next" button at the bottom right of the search page. 
def profiles_loop():
    
    find_profiles()
    sleep(30)

    next_button = driver.find_element_by_xpath('//*[@id="pnnext"]') 
    next_button.click()
    sleep(30)

    
def repeat_fun(times, f):
    for i in range(times): f()
    
# specifies the path to the chromedriver.exe
driver = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')


# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')



# locate email form by_class_name
username = driver.find_element_by_xpath('//input[@id="username"]')
username.send_keys('testemai378@gmail.com')

username = driver.find_element_by_xpath('//input[@id="password"]')
username.send_keys('testemai378123')

#click login
find = driver.find_element_by_xpath("//button[contains(text(),'Sign in')]")
find.click()
#Skip
#find = driver.find_element_by_xpath("//button[contains(text(),'Skip')]")
#find.click()


# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.google.com')
sleep(3)


# locate search form by_name
search_query = driver.find_element_by_name('q')

# send_keys() to simulate the search text key strokes
search_query.send_keys('site:linkedin.com/in/ AND "Technical Recruiter" AND "Ho Chi Minh City, Vietnam"')

sleep(8)

driver.get('https://uk.linkedin.com/in/pauljgarner')

driver.page_source



# .send_keys() to simulate the return key 
search_query.send_keys(Keys.RETURN)



soup = BeautifulSoup(driver.page_source,'lxml')
result_div = soup.find_all('div', attrs={'class': 'g'})
    
# initialize empty lists
links = []
titles = []
descriptions = []

# Function call x10 of function profiles_loop; you can change the number to as many pages of search as you like. 
repeat_fun(2, profiles_loop)

print(titles)
print(links)

# Separates out just the First/Last Names for the titles variable
titles01 = [i.split()[0:2] for i in titles]

# The function below stores scraped data into a .csv file
from itertools import zip_longest
# Load titles and links data into csv
d = [titles01, links]
export_data = zip_longest(*d, fillvalue = '')
with open(parameters.file_name, 'w', encoding="ISO-8859-1", newline='') as myfile:
      wr = csv.writer(myfile)
      wr.writerow(("Titles", "Links", "Current_Job", "Current_Location" ))
      wr.writerows(export_data)
myfile.close()
