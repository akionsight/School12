# Write a database connectivity program to insert a new student record to student table (rno, name avg)

import mysql.connector as connector 

conn = connector.connect(user="root", passwd="123", database="test", host="localhost")
cursor = conn.cursor()

rno = int(input("Enter rno of student: "))
name = input("Enter name of student: ")
avg = int(input("Enter avg marks of student: "))

cursor.execute(f"INSERT INTO student (rno, name, avg) VALUES ({rno}, {name}, {avg})")
conn.commit()