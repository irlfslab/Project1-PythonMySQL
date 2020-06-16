# 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root',
    database ='PyDB_Demo'
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

# DROP a Database:
my_cursor.execute("DROP DATABASE IF EXISTS PyDB_Demo")






