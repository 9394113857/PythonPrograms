import sqlite3

# Establish a connection to the database
conn = sqlite3.connect('calculator.db')

# Create a cursor object
c = conn.cursor()

# Execute a CREATE TABLE statement
c.execute('''CREATE TABLE IF NOT EXISTS calculations
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              num1 REAL, 
              num2 REAL, 
              operation TEXT, 
              result REAL,
              date DATE,
              time TIME,
              email TEXT)''')

# Commit the changes to the database
conn.commit()

# Close the connection
conn.close()
