import mysql.connector as myconn

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
)

mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE mydatabase")
print(mydb)

# command to show all Databases in my database
mycursor.execute("SHOW DATABASES")

for i in mycursor:
    print(i)


# try to connecting the database 

mydb = myconn.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)
print("data base is connected successfull")