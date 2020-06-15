# 1. importing MySQL Connector package:
import mysql.connector

# 2. Create Connection
mydb = mysql.connector.connect (
    host="localhost",
    user='root',
    passwd='root',
    database='PyDB_Demo'
)

# 3. Creating an instance of a cursor
my_cursor = mydb.cursor()

# Select With a Filter (conditional Statement)
my_cursor.execute("SELECT * FROM employees WHERE first_name like 'v%' order by first_name")

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

# for test
print (result)

print("-------------------------------")
print("| First Name starts with 'v'  |")
print("|     Sort by First name      |")
print("-------------------------------")
# Display them with a nice format and labels: 
for record in result:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')


# Select With a Filter (conditional Statement)
my_cursor.execute("SELECT * FROM employees WHERE last_name like '%he%' order by last_name")

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

# for test
print (result)

print("----------------------------")
print("| Last Name contains 'he'  |")
print("|    Sort by Last Name     |")
print("----------------------------")
# Display them with a nice format and labels:
for record in result:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')

# Select With a Filter (conditional Statement)
my_cursor.execute("SELECT * FROM employees WHERE date_hired < '2000-12-31' or salary > 45000 order by date_hired")

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

# for test
print (result)

print("----------------------------------------------")
print("| Date Hired < 2000-12-31 or Salary > 45000  |")
print("|            Sort by Date Hired              |")
print("----------------------------------------------")
# Display them with a nice format and labels:
for record in result:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')

# Select With a Filter (conditional Statement)
my_cursor.execute("SELECT * FROM employees WHERE salary > 30000 and job_title like 'd%' order by salary desc")

# Note: We use the fetchall() method, which fetches all rows from the last executed statement.
result =my_cursor.fetchall()

# for test
print (result)

print("------------------------------------------------")
print("| Salary > 30000 and Job Title start with 'd'  |")
print("|          Sort by descending salary           |")
print("--------------------------------------- --------")
# Display them with a nice format and labels:
for record in result:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')
