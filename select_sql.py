import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()


mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#  to fetch only one row
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print("\n The one row is ",myresult)


