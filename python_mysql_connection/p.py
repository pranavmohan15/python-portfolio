import mysql.connector

con=mysql.connector.connect(
    user='root',
    password='Annex@2025',
    host='localhost',
    port=3306,
    database='test'
)

cur=con.cursor()

q="update students set course_id=%s where student_name=%s"
v=(102,'pranav')
cur.execute(q,v)
con.commit()

print("updated",cur.rowcount)

select_q="select * from courses"
cur.execute(select_q)
rows=cur.fetchall()
for i in rows:
    print(i)

cur.close()
con.close()