import mysql.connector
import datetime

def get_connection():
    return mysql.connector.connect(
        user='root',
        password='Annex@2025',
        host='localhost',
        port=3306,
        database='project'
    )
def list_accounts():
    con=get_connection()
    cur=con.cursor()
    cur.execute("select id,name,opening_balance from accounts order by id")
    rows=cur.fetchall()
    cur.close()
    con.close()
    return rows

def account_balance(account_id):
    con=get_connection()
    cur=con.cursor()
    cur.execute("SELECT opening_balance from accounts where id=%s",(account_id,))
    r=cur.fetchone()
    if not r:
        cur.close()
        con.close()
        return None
    bal=float(r[0])
    cur.execute("SELECT SUM(amount) FROM transactions WHERE account_id=%s AND type='income'",(account_id,))
    inc=cur.fetchone()[0]
    if inc is None:
        inc = 0
    cur.execute("SELECT SUM(amount) FROM transactions WHERE account_id=%s AND type='expense'",(account_id,))
    exp = cur.fetchone()[0]
    if exp is None:
        exp = 0
    cur.close()
    con.close()
    return bal+float(inc)-float(exp)

def list_categories(filter_type=None):
    con=get_connection()
    cur=con.cursor()
    if filter_type:
        cur.execute("SELECT id,name FROM categories WHERE type=%s order by name",(filter_type,))
    else:
        cur.execute("SELECT id,name,type FROM categories order by name,type")
    rows=cur.fetchall()
    cur.close()
    con.close()
    return rows

def add_account():
    con=get_connection()
    cur=con.cursor()
    name=input("Enter your Account Name:")
    opening_balance=float(input("Enter your opening balance:"))
    q="insert into accounts(name,opening_balance) values(%s,%s)"
    v=(name,opening_balance)
    cur.execute(q,v)
    con.commit()
    print("Account added succesfully")
    cur.close()
    con.close()

def view_accounts():
    con=get_connection()
    cur=con.cursor()
    rows=list_accounts()
    if not rows:
        print("No Accounts Found")
        return
    for i in rows:
        bal=account_balance(i[0])
        print(f"ID:{i[0]} | NAME:{i[1]} | OPENING_BALANCE:{i[2]} | CURRENT_BALANCE:{bal:.2f}")
        print()

def add_category():
    con=get_connection()
    cur=con.cursor()
    name=input("Enter the name of the category:")
    type=input("Enter the type of the category:")
    q='insert into categories(name,type) values(%s,%s)'
    val=(name,type)
    cur.execute(q,val)
    con.commit()
    print("category added successfully!")
    cur.close()
    con.close()

def view_categories():
    rows=list_categories()
    if not rows:
        print("no categories found")
        return
    for i in rows:
        print(f"ID:{i[0]} | Name:{i[1]} | Type:{i[2]}")

def add_transaction():
    print("Select account:")
    accounts = list_accounts()
    if not accounts:
        print("No accounts. Add an account first.")
        return
    for a in accounts:
        print(f"{a[0]}: {a[1]} (opening {a[2]})")
    aid = int(input("Enter account id: ").strip())

    t = ""
    while t not in ("income", "expense"):
        t = input("Type (income/expense): ").strip().lower()

    print("Select category:")
    cats = list_categories(filter_type=t)
    if not cats:
        print("No categories of this type. Add a category first.")
        return
    for c in cats:
        print(f"{c[0]}: {c[1]}")
    cid = int(input("Enter category id: ").strip())

    amt = float(input("Enter amount: ").strip())
    note = input("Enter note (optional): ").strip() or None
    tx_date = datetime.date.today()


    if t == "expense":
        bal = account_balance(aid)
        if bal is None:
            print("Account not found.")
            return
        print(f"Current balance: {bal:.2f}")
        if amt > bal:
            print("Insufficient balance. Transaction rejected.")
            return

    conn = get_connection()
    cur = conn.cursor()
    q = """INSERT INTO transactions
           (account_id, category_id, type, amount, note, tx_date)
           VALUES (%s,%s,%s,%s,%s,%s)"""
    cur.execute(q, (aid, cid, t, amt, note, tx_date))
    conn.commit()
    print("Transaction recorded")
    cur.close()
    conn.close()

def view_transactions():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT t.id, t.tx_date, a.name, c.name, t.type, t.amount, t.note
                   FROM transactions t
                   JOIN accounts a ON t.account_id=a.id
                   JOIN categories c ON t.category_id=c.id
                   ORDER BY t.tx_date DESC, t.id DESC""")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        print("No transactions.")
        return
    for r in rows:
        print(f"ID:{r[0]} | Date:{r[1]} | Account:{r[2]} | Category:{r[3]} | {r[4]} | Amount:{r[5]} | Note:{r[6]}")

def monthly_summary():
    m = input("Enter month (YYYY-MM) or leave blank for current: ").strip()
    if m == "":
        today = datetime.date.today()
        m = today.strftime("%Y-%m")
    start = datetime.datetime.strptime(m + "-01", "%Y-%m-%d").date()
    if start.month == 12:
        end = datetime.date(start.year + 1, 1, 1)
    else:
        end = datetime.date(start.year, start.month + 1, 1)

    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT c.type, c.name, SUM(t.amount) FROM transactions t
                   JOIN categories c ON t.category_id=c.id
                   WHERE t.tx_date >= %s AND t.tx_date < %s
                   GROUP BY c.type, c.name
                   ORDER BY c.type, SUM(t.amount) DESC""", (start, end))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    if not rows:
        print("No transactions in this month.")
        return
    inc = 0; exp = 0
    for r in rows:
        typ = r[0]; cat = r[1]; s = r[2] or 0
        if typ == "income":
            inc += s
        else:
            exp += s
        print(f"{typ:7} | {cat:20} | {s:.2f}")
    print(f"Total income: {inc:.2f}  Total expense: {exp:.2f}  Net: {inc - exp:.2f}")



def menu():
    while(True):
        print('-----financial managemnt system-----\n1.ADD ACCOUNT\n2.VIEW ACCOUNT\n3.ADD CATEGORY\n4.VIEW CATEGORIES\n5.ADD TRANSACTIONS(Income,Expense)\n6.VIEW TRANSACTIONS\n7.MONTHLY SUMMARY\n8.EXIT')
        choice=int(input("Enter the choice:"))
        if choice==1:
            add_account()
        elif choice==2:
            view_accounts()
        elif choice==3:
            add_category()
        elif choice==4:
            view_categories()
        elif choice==5:
            add_transaction()
        elif choice==6:
            view_transactions()
        elif choice==7:
            monthly_summary()
        elif choice==8:
            print("BYE! SEE U AGAIN")
            break
        else:
            print("Enter a valid choice!!")
menu()
