import mysql.connector

con=mysql.connector.connect(
    user='root',
    password='Annex@2025',
    host='localhost',
    port=3306,
    database='demo'

)
cur=con.cursor()
q='delete from users where name=%s'
v=('niha',)

cur.execute(q,v)
con.commit()
print("deleted",cur.rowcount)

select_q = 'select * from users'
cur.execute(select_q)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
con.close()