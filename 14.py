import mysql.connector as connector 

conn = connector.connect(user="root", passwd="123", database="test", host="localhost")
cursor = conn.cursor()

cursor.execute('DELETE FROM students WHERE name = "Raj"')
conn.commit()