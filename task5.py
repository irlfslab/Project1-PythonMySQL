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

query = "Delete from employees WHERE emp_id=2" 

# my_cursor.execute('SQL Command')
my_cursor.execute(query)
mydb.commit()

print(my_cursor.rowcount, "record(s) deleted")

my_cursor.execute('SELECT * FROM employees')
print("----------------------------------------------------")
# Display them with a nice format and labels:
for record in my_cursor:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')

# Note: The update/delete will affect only the record(s) that match the WHERE condition