# importing MySQL Connector package:
import mysql.connector

# Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root'
)
# test the connection:
print(mydb)
# the output (result): <mysql.connector.connection.MySQLConnection object at 0x03B48160>

# Creating an instance of a cursor
my_cursor = mydb.cursor()

# 1. Create a new database
my_cursor.execute('CREATE DATABASE IF NOT EXISTS PyDB_Demo')

# 2.a. Show databases:
my_cursor.execute('SHOW DATABASES') 
print(my_cursor) # MySQLCursor: SHOW DATABASES
# loop through my_cursor
for db in my_cursor:
    # in every iteration we are going to print a database name
    print(db)

# 2.b. Use 'PyDB_Demo'
my_cursor.execute('USE PyDB_Demo')
print(my_cursor) # MySQLCursor: USE PyDB_Demo

# 3.  Create table 'employees'
my_cursor.execute("CREATE TABLE IF NOT EXISTS employees (emp_id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(40) NOT NULL, last_name VARCHAR(40) NOT NULL, email VARCHAR(50) NOT NULL UNIQUE, job_title VARCHAR(40) NOT NULL, date_hired DATE NOT NULL, salary DECIMAL(7,2) CHECK ( salary >= 15000 AND salary <=50000))")

# 4.  Show all tables in current database
my_cursor.execute('SHOW TABLES')
print(my_cursor)
for table in my_cursor:
     # in every iteration to print a table name
    print(table)