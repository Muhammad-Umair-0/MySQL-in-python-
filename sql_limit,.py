import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers LIMIT 5"

mycursor.execute(sql)

result =mycursor.fetchall()

for x in result:
    print(x)

# Start from position 3, and return 5 records:

sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"
mycursor.execute(sql)

myresult = mycursor.fetchall()
print("for offset output")
for x in myresult:
    print(x)