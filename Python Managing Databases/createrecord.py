import psycopg2 as db
conn_string="dbname='datawarehouse' host='localhost' user='postgres' password='admin'"
conn=db.connect(conn_string)
cur=conn.cursor()
query = "insert into usernames (id,name,street,city,zip) values({},'{}','{}','{}','{}')".format(1,'Jonathan Johnson','8121 Ryan Hills Suite 417','New Tonyview','99784')
print(cur.mogrify(query))
query2 = "insert into users (id,name,street,city,zip) values(%s,%s,%s,%s,%s)"
data=(1,1,'Jonathan Johnson','8121 Ryan Hills Suite 417','New Tonyview','99784')
print(cur.mogrify(query2,data))
cur.execute(query2,data)
conn.commit()



