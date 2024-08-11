import mysql.connector as connector 

conn = connector.connect(user="root", passwd="123", database="test", host="localhost")
cursor = conn.cursor()

rno = int(input("Enter rno of student: "))
new_name = input("Enter new name of student: ")

cursor.execute(f"UPDATE students SET name = {new_name} WHERE rno = {rno}")
