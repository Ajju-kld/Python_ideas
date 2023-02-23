import sqlite3

conn = sqlite3.connect('student.db')
print("Opened database successfully")

conn.execute(''' CREATE TABLE if not exists student (ID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL)''')
print("Table created successfully")
a=int(input("enter the number of records that you are adding: "))
inputs=[]
for i in range(a):
    print("details of " + str(i) +"th person")
    
    iD=int(input("enter the id: "))
    name=input("enter the name: ")
    age=int(input("enter the age"))
    inputs.append([iD,name,age])
for i in inputs:
    conn.execute("INSERT INTO student (ID, NAME, AGE) VALUES(?,?,?)",(i[0],i[1],i[2]))
    print(i[0])
conn.commit()
print("Records created successfully")

cursor = conn.execute("SELECT ID, NAME, AGE from student")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("AGE = ", row[2], "\n")

print("Operation done successfully")
conn.close()
