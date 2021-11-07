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
# Connect to PostgreSQL 
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=admin")
cur = conn.cursor()


###########################################################
# Merge all Csv from Linkedin Output Folder
path = r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\Indeed\outputs' # use your path
all_files = glob.glob(path + "/*.csv")

full_list_indeed = []

for filename in all_files:
    df = pd.read_csv(filename)
    full_list_indeed.append(df)

frame = pd.concat(full_list_indeed, axis=0, ignore_index=True)
print((frame).head())

frame.rename(columns={'Unnamed: 0': 'auto_id'}, inplace=True)
for col in frame.columns:
    print(col)
 
###########################################################
# Pre Cleaning check for duplicates 

frame.drop_duplicates(subset=['Link'])



############################################################    
# TO REMOVE
    
frame.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\Indeed\outputs\outputsall.csv',encoding='utf-8-sig')


