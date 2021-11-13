# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 20:15:22 2021

@author: renau
"""
# Import Librairies
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
import glob
from io import StringIO
import prettytable
import os
import sys
import time
import numpy as np
from timeit import default_timer as timer
from googletrans import Translator

translator=Translator()
# Delete previous file
#################################################################
file = r'C:\\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\Vietnamworks\outputs\Results\outputsall.csv'
if(os.path.exists(file) and os.path.isfile(file)):
  os.remove(file)
  print("file deleted")
else:
  print("file not found")


###########################################################
# Merge all Csv from Vietnam work Output Folder
path = r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\Vietnamworks\outputs\Raw' # use your path
all_files = glob.glob(path + "/*.csv")

full_list_vietnamworks = []

for filename in all_files:
    df = pd.read_csv(filename)
    full_list_vietnamworks.append(df)

frame = pd.concat(full_list_vietnamworks, axis=0, ignore_index=True)
print((frame).head())

# TO DELETE TEST ONLY


########################################################################################################
# Pre Cleaning check for duplicates Links
frame = frame.drop(frame.columns[[0]], axis=1)  # df.columns is zero-based pd.Index
frame.drop_duplicates(subset=['Link'])

#Lower Caps all text 
frame['Title'] = frame['Title'].str.lower()
print(frame['Title'].head())


#Remove rows where CONTAINS ->
frame = frame[~frame['Title'].isin(['data entry'])]
print(frame.info())




# Translate job name
#frame['TitleEnglish'] = frame['Title'].apply(translator.translate, src='vi', dest='en').apply(getattr, args=('text',))


# Output Frame to CSV
print(frame.info())
frame.to_csv(r'C:\Users\renau\OneDrive\02-Data Projects\01-Data-Engineering\webscrapping\Vietnamworks\outputs\Results\outputsall.csv',encoding='utf-8-sig')



# clean cities

### ................



################################################################        (Updates Insert only new rows)
#INPUT YOUR OWN CONNECTION STRING HERE
#conn_string = 'postgres://postgres:admin@localhost/postgres'


#perform to_sql test and print result
#db = create_engine(conn_string)
#conn = db.connect()

#start_time = time.time()
#frame.to_sql('Linkedinjob', con=conn, if_exists='append', index=False)
#print("to_sql duration: {} seconds".format(time.time() - start_time))
#print("COPY duration: {} seconds".format(time.time() - start_time))



#close connection
#conn.close()

