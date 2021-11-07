# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:15:22 2021

@author: renau
"""
# Import Librairies
import psycopg2
import pandas as pd
import glob
from io import StringIO
import prettytable
import os

# Delete previous file
#################################################################
file = r'C:\\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\outputsall.csv'
if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)
  print("file deleted")
else:
  print("file not found")


#################################################################
# Connect to PostgreSQL 
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=admin")
cur = conn.cursor()


###########################################################
# Merge all Csv from Linkedin Output Folder
path = r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs' # use your path
all_files = glob.glob(path + "/*.csv")

full_list_linkedin = []

for filename in all_files:
    df = pd.read_csv(filename)
    full_list_linkedin.append(df)

frame = pd.concat(full_list_linkedin, axis=0, ignore_index=True)
print((frame).head())

frame.rename(columns={'Unnamed: 0': 'auto_id'}, inplace=True)
for col in frame.columns:
    print(col)

###########################################################
# Pre Cleaning check for duplicates Links

frame.drop_duplicates(subset=['Link'])



#Lower Caps all text 
frame = frame.drop_duplicates(subset=['Link'])
frame['Title'] = frame['Title'].str.lower()
print(frame['Title'].head())


#Remove rows where CONTAINS ->
frame = frame[~frame['Title'].isin(['data entry'])]
print(frame.info())



# Output Frame to CSV
print(frame.info())
frame.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\linkedin\outputs\outputsall.csv',encoding='utf-8-sig')