import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()
sql = 