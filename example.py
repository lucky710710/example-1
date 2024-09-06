import sqlite3  # Import the sqlite3 library to work with SQLite databases

conn = sqlite3.connect('online_store.db')  # Creates/opens a database named 'online_store.db'
cursor = conn.cursor()  # Create a cursor object to execute SQL commands

cursor.execute('''CREATE TABLE IF NOT EXISTS products
                  (ProductID INTEGER PRIMARY KEY,  
                   Name TEXT,
                   Description TEXT, 
                   Price REAL,  
                   StockQuantity INTEGER)''')  # Quantity of the product in stock

cursor.execute("INSERT INTO products (Name, Description, Price, StockQuantity) VALUES (?, ?, ?, ?)", 
               ('Laptop', 'A high-performance laptop', 999.99, 50))  # Add a sample product entry

conn.commit()  # Save the changes to the database

cursor.execute("SELECT * FROM products")  # Retrieve all rows from the products table
rows = cursor.fetchall()  # Fetch all results from the executed query

for row in rows:  # Loop through each row in the fetched result set
    print(row)  # Print the current row (each product)

conn.close()  # Close the database connection to free up resources