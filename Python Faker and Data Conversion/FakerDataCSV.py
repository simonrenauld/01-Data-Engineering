# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#libraries
import pandas as pd
from faker import Faker
import csv
output=open('data.CSV','w')
fake=Faker()
header=['name','age','street','city','state','zip','lng','lat']
mywriter=csv.writer(output)
mywriter.writerow(header)
for r in range(1000):
    mywriter.writerow([fake.name(),fake.random_int(min=18,
    max=80, step=1), fake.street_address(), fake.city(),fake.
    state(),fake.zipcode(),fake.longitude(),fake.latitude()])
output.close()



#read data
df = pd.read_csv('data.csv', sep='\t')
print(df.head(10))

#Dictionary of data
df=pd.DataFrame(df)
df.to_csv('fromdf.CSV',index=False)