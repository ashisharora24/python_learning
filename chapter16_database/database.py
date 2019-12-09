'''
    INSTALL FOLLOWING
    syntax :
        pip install mysql-connector-python
'''

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
''' fetch ONE ROW AT A TIME from database '''

import mysql.connector

conn = mysql.connector.connect(
                host = 'localhost',
                database = 'urbanclap',
                user = 'root',
                password = 'admin'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

cursor.execute("select * from uc")

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
                database = 'urbanclap',
                user = 'root',
                password = 'admin'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

cursor.execute("select * from uc")

### getting one row at a time
rows = cursor.fetchall()

print("row count : ", cursor.rowcount)

for row in rows:
    print(row)

cursor.close()
conn.close()

# # ------------------------------------------------------------------------------
#
# ''' INSERT STATEMENT '''
#
import mysql.connector

conn = mysql.connector.connect(
                host = 'localhost',
                database = 'urbanclap',
                user = 'root',
                password = 'admin'
                )

if conn.is_connected():
    print("connected to mysql")

cursor = conn.cursor()

try:
    str = 'INSERT INTO test (test)  VALUES (3)'
    cursor.execute(str)
    conn.commit()
    print(cursor.rowcount, "record inserted.")
except:
    conn.rollback()
    print("failed")

cursor.close()
conn.close()
