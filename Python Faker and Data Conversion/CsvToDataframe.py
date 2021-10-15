# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 11:19:14 2021

@author: renau
"""

#libraries
import pandas as pd
import numpy as np

#read data
df = pd.read_csv('data.csv', sep='\t')
print(df.head(10))

#Dictionary of data
df=pd.DataFrame(df)
df.to_csv('fromdf.CSV',index=False)
