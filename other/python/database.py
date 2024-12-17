import sqlite3
# Connect to Database ********************
conn = sqlite3.connect('customer.db')

# Create a cursor  ********************

c = conn.cursor()

# Create Table ********************

# c.execute('''
#       CREATE TABLE customers (
#         first_name text,
#         last_name text,
#         email text
#       )
# ''')

# Insert into Table ********************

# many_customers = [
#       ('Lokal', 'Doe', 'lokal@me.com'),
#       ('Jane', 'Smith', 'jane@me.com'),
#       ('Bob', 'Smith', 'bob@me.com')
# ]

# c.execute("INSERT INTO customers VALUES ('Brown', 'Doe', 'Brown@example.com')")
# c.executemany("INSERT INTO customers VALUES (?, ?, ?)", many_customers)

# print("Customer Added successfully...")

# Datatype => (# NULL# INTEGER # REAL # TEXT # BLOB)

# Query the database ********************

# c.execute("SELECT * FROM customers")
# print(c.fetchall())
# print(c.fetchone()[0])
# print(c.fetchone())
# print(c.fetchmany(3))

# items = c.fetchall()
# print("NAME" + "\t\t\tEMAIL")
# print("********" + "\t\t********")
# for item in items:
#       print(item[0] + " " + item[1] + "\t\t" + item[2])

# c.execute("SELECT rowid, * FROM customers")
# c.execute("SELECT * FROM customers WHERE last_name = 'Doe'")
# items = c.fetchall()
# for item in items:
#       print(item)

# Update Records ******************** 

# c.execute('''
#       UPDATE customers SET 
#           first_name = 'ABA'
#       WHERE rowid = 1
      
# ''')

# # Delete Records ******************** 

# c.execute('''
#       DELETE FROM customers WHERE rowid = 2
# ''')

# Query The Database ORDER BY ******************** 

c.execute("SELECT rowid, * FROM customers ORDER BY last_name ASC")
items = c.fetchall()
for item in items:
      print(item)
# Commit our command
conn.commit()
# Close our connection 
conn.close()