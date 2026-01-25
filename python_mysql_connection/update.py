import mysql.connector

con=mysql.connector.connect(
    user='root',
    password='Annex@2025',
    host='localhost',
    port=3306,
    database='demo'

)
cur=con.cursor()
q="update users set age=%s  where name=%s"
v=(10,'noufal')

cur.execute(q,v)
con.commit()

print("Updated:",cur.rowcount)

select_q = 'select * from users'
cur.execute(select_q)
rows = cur.fetchall()

for i in rows:
    print(i)


cur.close()
con.close()

