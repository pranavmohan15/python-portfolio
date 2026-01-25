import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user='root',
        password='Annex@2025',
        port=3306,
        host='localhost',
        database='sep_22'
    )

def create_contact():
    conn=get_connection()
    cur=conn.cursor()
    name=input("enter yout name:")
    address=input("enter yout address:")
    phone=int(input("enter your phone number:"))
    q='insert into contacts(name,address,phone_number)values(%s,%s,%s)'
    val=(name,address,phone)
    cur.execute(q,val)
    conn.commit()
    print("Data Added Successfully")
    cur.close()
    conn.close()

def read_contact():
    conn=get_connection()
    cur=conn.cursor()
    print("---Display all Details")
    cur.execute('select * from contacts')
    row=cur.fetchall()
    for i in row:
        print(f"ID:{i[0]} | NAME:{i[1]} | ADDRESS:{i[2]} | PHONE:{i[3]}")
        print()
    cur.close()
    conn.close()

def update_details():
    conn=get_connection()
    cur=conn.cursor()
    id=int(input("enter the id you want to update:"))
    q1="select id from contacts where id=%s"
    val1=(id,)
    cur.execute(q1,val1)
    result = cur.fetchone()
    if not result:
        print("ID does not exist. No update performed.")
        cur.close()
        conn.close()
        return
    new_name=input("enter the new name:")
    new_address=input("enter the new address:")
    new_phone=int(input("enter your phone:"))
    q="update contacts set name=%s,address=%s,phone_number=%s where id=%s"
    val=(new_name,new_address,new_phone,id)
    cur.execute(q,val)
    conn.commit()
    print("data updated successfully!")
    cur.close()
    conn.close()

def delete_data():
    conn=get_connection()
    cur=conn.cursor()
    id=int(input("enter the id you want to delete:"))
    query1="select id from contacts where id=%s"
    value1=(id,)
    cur.execute(query1,value1)
    result=cur.fetchone()
    if not result:
        print("The Id Is Not Exist In Our Table!")
        cur.close()
        conn.close()
        return
    
    q='delete from contacts where id=%s'
    val=(id,)
    cur.execute(q,val)
    conn.commit()
    print("deleted succesfully")
    cur.close()
    conn.close()

def menu():
    while(True):
        print('----contact Details----\n1.Add new contact\n2.view contach details\n3.update details\n4.delete details')
        choice=int(input("enter a choice:"))

        if choice==1:
            create_contact()
        elif choice==2:
            read_contact()
        elif choice==3:
            update_details()
        elif choice==4:
            delete_data()
        elif choice==5:
            break
        else:
            print("invalid choice!")
menu()