
        
##Import Statement
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path=r'C:/Users/bin/chromedriver')                         #path for Chromedriver
google_page = driver.get('https://www.google.com')                  #Opens a google page in chrome browser
search_box = driver.find_element_by_xpath('//input[@name="q"]')     # Find the google search box
search_box.send_keys('Python')                                      #Enter the keyword  "Python"
search_box.send_keys(Keys.ENTER)                                    #Clicks the search button

pages_links =[]

## Getting links from first 4 pages in google search result
counter = 0

for i in range(counter,4):

	page_no = driver.find_elements_by_xpath("//table[@class='AaVjTc']/tbody/tr/td/a")   # Get the pages links which is at the bottom
	page_no[i].click()                                                                  #Click that page to go that page

	value = driver.find_elements_by_xpath('//div[@class="r"]/a')                        #Gets Links of that page

	## Loop for getting the href value of all the links in search result
	for each_val in value:
		link = each_val.get_attribute('href')
		pages_links.append(link)
print("Complete links of four pages","\n".join(pages_links))
driver.quit()                       #Close the browser window.        