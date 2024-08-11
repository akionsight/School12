import mysql.connector as connector 

conn = connector.connect(user="root", passwd="123", database="test", host="localhost")
cursor = conn.cursor()

cursor.execute("select * from students")
for record in cursor.fetchall():
    print(record)

## SAME AS QUESTION 11, MAYBE