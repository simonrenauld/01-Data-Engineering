# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:22:06 2021

@author: renau
"""

from faker import Faker
import json
import pandas as pd
import pandas.io.json as pd_JSON

### create fake json data
output=open('data.JSON','w')
fake=Faker()

alldata={}
alldata['records']=[]

#important to indent all data
for x in range(1000):
    data={"name":fake.name(),"age":fake.random_int
        (min=18, max=80, step=1),
        "street":fake.street_address(),
        "city":fake.city(),"state":fake.state(),
        "zip":fake.zipcode(),
        "lng":float(fake.longitude()),
        "lat":float(fake.latitude())}
    alldata['records'].append(data)

json.dump(alldata,output)

#load and read Json Data
import json
with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

f=open('data.JSON','r')
data=pd_JSON.loads(f.read())

# Dataframe back to JSON
#working with JSON that is oriented around records makes processing it
#in tools such as Airflow much easier than JSON in other formats, such as split, index,
#columns, values, or table. 


df=pd_JSON.json_normalize(alldata,record_path='records')
df.head(2).to_json()