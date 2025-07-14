import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor  = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# if the table already exists, it will not create it again  
mycursor.execute("SHOW TABLES")
for table in mycursor:
    print(table)

# Remove or comment out this line, since 'id' already exists
# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# inset the values into The Table using INSERT INTO
mycursor.execute("INSERT INTO customers (name, address) VALUES('Umair', 'Lahore')")
# val = ('Ali', 'Karachi')
# mycursor.execute(sql, val) #for single record insertion
mydb.commit()

print(mycursor.rowcount, "record inserted.")

# insert multiple records into the table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
    ('Ali', 'Karachi'),
    ('Sara', 'Islamabad'),
    ('John', 'New York')
]

mycursor.executemany(sql, val)

mydb.commit()
print(mycursor.rowcount, "records inserted.")

# get inserted id
print(mycursor.lastrowid)

# Fetching all records from the table
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)

