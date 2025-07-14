import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Umair.1321",
    database = "mydatabase"
)

mycursor = mydb.cursor()

# Create products table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
)
""")

# Create users table
mycursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    fav INT,
    FOREIGN KEY (fav) REFERENCES products(id)
)
""")

# Insert sample data if tables are empty
mycursor.execute("SELECT COUNT(*) FROM products")
if mycursor.fetchone()[0] == 0:
    mycursor.executemany(
        "INSERT INTO products (name) VALUES (%s)",
        [("Chocolate",), ("Vanilla",), ("Strawberry",)]
    )
    mydb.commit()

mycursor.execute("SELECT COUNT(*) FROM users")
if mycursor.fetchone()[0] == 0:
    mycursor.executemany(
        "INSERT INTO users (name, fav) VALUES (%s, %s)",
        [("Ali", 1), ("Sara", 2), ("John", 3)]
    )
    mydb.commit()

# Now run the join query
sql = """
SELECT users.name AS user, products.name AS favorite_product
FROM users
INNER JOIN products ON users.fav = products.id
"""

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
    print(x)

