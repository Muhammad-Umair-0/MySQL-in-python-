import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()


sql =  "SELECT * FROM customers WHERE address = 'Lahore'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)  

#  wild card character
sql = "SELECT * FROM customers WHERE address LIKE 'L%'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("\nRecords with address starting with 'L':")
for x in myresult:  
    print(x)

# to prevent SQL injetion,
sql = "SELECT * FROM customers WHERE address = %s"
VAL = ("lahore", )
mycursor.execute(sql, VAL)
result = mycursor.fetchall()
print("\n Records with injection prevention:")
for x in result:
    print(x)

# sort the reesults order by name

sql =  "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
result = mycursor.fetchall()
print("\nRecords sorted by name:")
for x in result:
    print(x)

# sort the record in Descending order
sql =  "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
print("\n print all the results  in Descending order \n")
for x in myresult:
    print(x)


