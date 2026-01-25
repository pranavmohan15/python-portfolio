import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user='root',
        password='Annex@2025',
        host='localhost',
        port=3306,
        database='sep_22'

    )
def mark_add():
    con=get_connection()
    cur=con.cursor()
    q='insert into marksheet(name,mark)values(%s,%s)'
    v=('pranav',27)
    cur.execute(q,v)
    con.commit()
    print("mark added successfully")
    cur.close()
    con.close()
def view_mark():
    con=get_connection()
    cur=con.cursor()
    cur.execute("select * from marksheet")
    row=cur.fetchall()
    for i in row:
        print(f"ID:{i[0]} | NAME:{i[1]} |  MARK:{i[2]}")
    cur.close()
    con.close()
def update_mark():
    con=get_connection()
    cur=con.cursor()
    id=int(input("enter the id:"))
    
    q1="select id from marksheet where id=%s"
    val=(id,)
    cur.execute(q1,val)
    result=cur.fetchone()
    if not result:
        print("the id is not  exist!")
        cur.close()
        con.close()
        return
    mark=int(input("enter the mark:"))
    q2="update marksheet set mark=%s where id=%s"
    val2=(mark,id)
    cur.execute(q2,val2)
    con.commit()
    print("data updated succesully")
    cur.close()
    con.close()

def delete_mark():
    con=get_connection()
    cur=con.cursor()
    id=int(input("enter the student id you want to delete:"))
    q="select id from marksheet where id=%s "
    v=(id,)
    cur.execute(q,v)
    result=cur.fetchone()
    if not result:
        print("the id is not exist!")
        cur.close()
        con.close()
        return
    q1="delete from marksheet where id=%s"
    val=(id,)
    cur.execute(q1,val)
    con.commit()
    print("deleted succesfully")
    cur.close()
    con.close()



def menu():
    while(True):
        print('----MARK DETAILS---\n1.add markdetails\n2.view mark details\n3.update mark details\4.delete mark details')
        choice=int(input("enter the choice:"))
        if choice==1:
            mark_add()
        elif choice==2:
            view_mark()
        elif choice==3:
            update_mark()
        elif choice==4:
            delete_mark()
        elif choice==5:
            print("BYE!")
            break
        else:
            print("invalid choice!")
menu()