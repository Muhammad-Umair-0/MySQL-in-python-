import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()
# used to drop the table 
# sql = "DROP TABLE customers"
# mycursor.execute(sql)


# drop only if exist 

sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql)
