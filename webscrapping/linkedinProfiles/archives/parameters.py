# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:12:07 2021

@author: renau
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from bs4.element import Tag
from time import sleep
import csv
from parsel import Selector
import parameters
import numpy

# search query 
search_query = 'site:linkedin.com/in/ AND "Recruiter" AND "Ho Chi Minh City, Vietnam"'


# file were scraped profile information will be stored  
file_name = 'results_file.csv'

# login credentials
linkedin_username = 'testemai378@gmail.com'
linkedin_password = 'testemai378123'

