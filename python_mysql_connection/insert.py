import mysql.connector

con=mysql.connector.connect(
    user='root',
    password='Annex@2025',
    host='localhost',
    port=3306,
    database='demo'
)
cur=con.cursor()

# story the query into q and value into v

q="insert into users(name,age) values(%s,%s)"
v=[
    ('pranavm',23),
    ('noufu',24),
    ('fil',30),
    ('p mohan',40)
]

cur.executemany(q,v)
con.commit()

print("inserted:",cur.rowcount)

select_q = 'select * from users'
cur.execute(select_q)
rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
con.close()
