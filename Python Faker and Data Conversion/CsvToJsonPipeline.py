# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:04:42 2021

@author: renau
"""

# =============================================================================
# #librairies
# conda install -c conda-forge airflow
#pip install apache-airflow-providers-ssh
# =============================================================================
from datetime import timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG
# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import datetime as dt

import pandas as pd
# =============================================================================
# read a CSV file and print out the names
# =============================================================================

def CSVToJson():
    df=pd.read_CSV('C:/Users/renau/OneDrive/02.Data Projects/01. Data Engineering/Python.csv')
    for i,r in df.iterrows():
        print(r['name'])
    df.to_JSON('fromAirflow.JSON',orient='records')
    
    default_args = {
        'owner': 'paulcrickard',
        'start_date': dt.datetime(2020, 3, 18),
        'retries': 1,
        'retry_delay': dt.timedelta(minutes=5),
        }
    
    with DAG('MyCSVDAG',
                default_args=default_args,
                schedule_interval=timedelta(minutes=5),
                # '0 * * * *',) as dag:
                print_starting = BashOperator(task_id='starting',
                bash_command='echo "I am reading the CSV now....."')
                CSVJson = PythonOperator(task_id='convertCSVtoJson', python_callable=CSVToJson)