import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="$tralaxia",
  database="csb"
)

mycursor = mydb.cursor()
mycursor.execute("select * from Book")
e=mycursor.fetchone()
print(e)
