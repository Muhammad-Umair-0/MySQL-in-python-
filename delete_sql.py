import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()
# sql = "DELETE FROM customers WHERE address = 'Karachi'"
# mycursor.execute(sql)
# mydb.commit()

# print( mycursor.rowcount)

# to prevent injection to escape Characters

sql =  "DELETE FROM customers WHERE address= %s"
adr = ("New York",)

mycursor.execute(sql, adr)
mydb.commit()
print(mycursor.rowcount, "records Deleted" )
