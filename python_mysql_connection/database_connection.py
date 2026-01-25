import mysql.connector
from prettytable import PrettyTable

connt=mysql.connector.connect(
    user='root',
    password='Annex@2025',
    port=3306,
    host='localhost',
    #database='demo'
)
mycursor=connt.cursor()

query='SHOW DATABASES'
mycursor.execute(query)

#generate table
table=PrettyTable()

table.field_names=["DATABASES"]

for db in mycursor.fetchall():
    table.add_row([db[0]])

print(table)

# for i in mycursor.fetchall():
#     print(i[0])

connt.close()