import psycopg2 as db
import pandas as pd
conn_string="dbname='postgres' host='host.docker.internal' port='5433' user='postgres' password='admin'"
conn=db.connect(conn_string)
df=pd.read_sql("select * from datawarehouse.employee", conn)
print(df.head())
print(df['id'].value_counts())
