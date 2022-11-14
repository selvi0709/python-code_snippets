# Ques:
# To create two tables in mysql db
# To populate records using python code
# To write joins to join two tables and display

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Mysql@123",
  database="courses"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE courses")

# print("Database is created")

# Creating Courses Table

query1 = "CREATE TABLE list (s_no INT, course_name VARCHAR(255), course_no INT, technology VARCHAR(255), price INT)"
mycursor.execute(query1)

sql1 = "INSERT INTO list (s_no, course_name, course_no, technology, price) VALUES (%s, %s, %s, %s, %s)"
val1 = [
  (1, 'Python', 101, 'web', 300),
  (2, 'HTML', 201, 'UI', 200),
  (3, 'SQL', 301, 'DB', 500),
  (4, 'MongoDB', 401, 'DB', 300)
]

mycursor.executemany(sql1, val1)
mydb.commit()
print(mycursor.rowcount, "courses was inserted")

mycursor.execute("SELECT * FROM list")
result = mycursor.fetchall()
print("Printing courses list")
for x in result:
  print(x)


# Creating Users Table

query2 = "CREATE TABLE users (s_no INT, user_id INT, user_name VARCHAR(255), age INT, enrolled VARCHAR(255))"
mycursor.execute(query2)

sql2 = "INSERT INTO users (s_no, user_id, user_name, age, enrolled) VALUES (%s, %s, %s, %s, %s)"
val2 = [
  (1, 101, 'Doi', 27, 'yes'),
  (2, 102, 'Selvi', 24, 'yes'),
  (3, 103, 'Jaya', 14, 'no'),
  (4, 104, 'Ajith', 25, 'yes')
]

mycursor.executemany(sql2, val2)
mydb.commit()
print(mycursor.rowcount, "users was inserted")

mycursor.execute("SELECT * FROM users")
result = mycursor.fetchall()
print("Printing users list")

for x in result:
  print(x)


print("list and users tables are created")

# JOINS

join = "SELECT users.user_name AS name, users.enrolled AS enrolled, list.course_name AS course FROM users JOIN list ON users.s_no=list.s_no where enrolled = 'yes'"

mycursor.execute(join)

result = mycursor.fetchall()

for x in result:
  print(x)
