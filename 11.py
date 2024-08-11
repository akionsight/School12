"""
Write a database connectivity program to fetch all the records from student
table.
Rno Name Avg
100 Raj 76.6
101 Harish 89.6
102 Kiran 98.9
103 Vedanth 92.5
"""


import mysql.connector as connector 

conn = connector.connect(user="root", passwd="123", database="test", host="localhost")
cursor = conn.cursor()

cursor.execute("select * from students")
for record in cursor.fetchall():
    print(record)