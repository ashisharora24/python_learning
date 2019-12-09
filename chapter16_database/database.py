''' fetch ONE ROW AT A TIME from database '''

import mysql.connector

conn = mysql.connector.connect(
                host = 'localhost',
                database = 'world',
                user = 'root',
                password = 'nag123'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

cursor =execute("select * from abc")

### getting one row at a time
row = cursor.fetchone()

while row is not None:
    print(row)
    row = cursor.fetchone()

cursor.close()
conn.close()


# ------------------------------------------------------------------------------

'''
    fetch ALL ROWS at one time
'''


import mysql.connector

conn = mysql.connector.connect(
                host = 'localhost',
                database = 'world',
                user = 'root',
                password = 'nag123'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

cursor =execute("select * from abc")

### getting one row at a time
rows = cursor.fetchall()

print("row count : ", cursor.rowcount)

from row in rows:
    print(row)

cursor.close()
conn.close()

# ------------------------------------------------------------------------------

''' INSERT STATEMENT '''

import mysql.connector

conn = mysql.connector.connect(
                host = 'localhost',
                database = 'world',
                user = 'root',
                password = 'nag123'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

str = 'INSERT INTO abc (name) value ("ashish")'

try:
    cursor.execute(str)
    conn.commit()
    print("1 row inserted")
except:
    conn.rollback()

cursor.close()
conn.close()
