import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor = mydb.cursor()
# mycursor.execute("""
# CREATE TABLE IF NOT EXISTS customers (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255),
#     address VARCHAR(255)
# )
# """)
print("Table created or already exists.")

sql = "UPDATE customers SET address = 'BHERA' WHERE address = 'Karachi' "
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "records effected")