
import mysql.connector

con=mysql.connector.connect(
    user='root',
    password="Annex@2025",
    host='localhost',
    port=3306,
    database='sep_22'

)

cur=con.cursor()
q_create='create table contactbook(id int auto_increment primary key,name varchar(50),address varchar(50),phone varchar(50))'
cur.execute(q_create)

q_insert='insert into contactbook(name,address,phone) values(%s,%s,%s)'
values=('pranav','ksd',12354525)
cur.execute(q_insert,values)
con.commit()

print("table created successfully")

cur.close()
con.close()