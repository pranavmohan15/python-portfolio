import mysql.connector

con=mysql.connector.connect(
    user='root',
    password="Annex@2025",
    host='localhost',
    port=3306,
    database="test"
)
print("connected")

cur=con.cursor()
q="CREATE TABLE student1(id int primary key,name varchar(200),subject varchar(200))"
cur.execute(q)
con.commit()

print("created")

cur.close()
con.close()
