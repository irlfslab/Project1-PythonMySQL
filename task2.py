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

sql_query = 'INSERT INTO employees (first_name,last_name,email,job_title,date_hired,salary) VALUES (%s,%s,%s,%s,%s,%s)'

many_record_values = [
    ('Peter', 'Smith', 'peters@email.ca', 'clerk', '2000-01-10', 20000),
    ('Amy', 'Clark', 'amyc@email.ca', 'designer', '2001-02-03', 40000),
    ('Viola', 'Che', 'voilac@email.ca', 'developer','2001-02-10', 35000),
    ('Vicky', 'Williams', 'vickyw@email.ca', 'manager', '2000-01-05', 50000)
]

my_cursor.executemany(sql_query,many_record_values)
mydb.commit()

# print ==> using the property "rowcount"
print(my_cursor.rowcount, "row(s) inserted")

my_cursor.execute("SELECT * FROM employees")

# We use the fetchall() method, which fetches all rows from the last executed statement.
result = my_cursor.fetchall()

print("----------------------------------------------------")
# Display them with a nice format and labels:
for record in result:
    print('Employee ID:', record[0])
    print('Full name:', record[1], record[2])
    print('Email:', record[3])
    print('Job Title:', record[4])
    print('Date Hired:', record[5])
    print('Salary:', record[6])
    print('**********************************')
