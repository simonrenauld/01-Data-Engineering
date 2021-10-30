import psycopg2 as db
from faker import Faker
fake=Faker()
data=[]
i=2

for r in range(1000):
    data.append((i,fake.name(),fake.street_address(),
                 fake.city(),fake.zipcode()))
    i+=1
    data_for_db=tuple(data)
    
conn_string="dbname='postgres' host='host.docker.internal' port='5433' user='postgres' password='admin'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "insert into datawarehouse.users (id,name,street,city,zip)values(%s,%s,%s,%s,%s)"
print(cur.mogrify(query,data_for_db[1]))

cur.executemany(query,data_for_db)
conn.commit()