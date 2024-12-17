import sqlite3

def create_products_table():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            barcode TEXT,
            unit_price REAL,
            sell_price REAL,
            qty_in_stock INTEGER
        )
    ''')

    conn.commit()
    conn.close()

def insert_product(product):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO products (name, barcode, unit_price, sell_price, qty_in_stock) VALUES (?, ?, ?, ?, ?)', product)

    conn.commit()
    conn.close()

class Product:
    def __init__(self, id, name, barcode, unit_price, sell_price, qty_in_stock):
        self.id = id
        self.name = name
        self.barcode = barcode
        self.unit_price = unit_price
        self.sell_price = sell_price
        self.qty_in_stock = qty_in_stock

    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, barcode={self.barcode}, unit_price={self.unit_price}, sell_price={self.sell_price}, qty_in_stock={self.qty_in_stock})"

def get_product_list():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = [Product(*row) for row in cursor.fetchall()]

    conn.close()
    return products

def save_product(product):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)',
                   (product.id, product.name, product.barcode, product.unit_price, product.sell_price, product.qty_in_stock))

    conn.commit()
    conn.close()

def find_product_by_id(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    row = cursor.fetchone()

    conn.close()
    if row:
        return Product(*row)
    else:
        return None

def update_product_by_id(product_id, **kwargs):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    update_fields = ', '.join([f"{field} = ?" for field, value in kwargs.items()])
    cursor.execute(f'UPDATE products SET {update_fields} WHERE id = ?', (*kwargs.values(), product_id))

    conn.commit()
    conn.close()

def delete_product_by_id(product_id):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_products_table()

    # Insert 10 products

    # products = [
    #     ('Laptop001', '1234567890123', 700.00, 9000.00, 10),
        # ('Smartphone', '9876543210987', 300.00, 400.00, 25),
        # ('Tablet', '4567891234567', 200.00, 250.00, 15),
        # ('Monitor', '5678901234567', 150.00, 200.00, 20),
        # ('Keyboard', '6789012345678', 25.00, 30.00, 50),
        # ('Mouse', '7890123456789', 15.00, 20.00, 60),
        # ('Printer', '8901234567890', 100.00, 120.00, 8),
        # ('Headphones', '9012345678901', 50.00, 70.00, 30),
        # ('Webcam', '0123456789012', 40.00, 55.00, 40),
        # ('External Hard Drive', '1123456789013', 60.00, 75.00, 18),
    # ]
    
    # for product in products:
    #     insert_product(product)

    # 1: Get Product List

    all_products = get_product_list()
    for product in all_products:
        print(product)
    
    # 2: Save a new product

    # new_product = Product(None, 'Gaming Chair', '2233445566778', 150.00, 200.00, 12)
    # save_product(new_product)
    # print("Product saved successfully.")
    
    # 3: Find the product by ID
    # product_id = 2
    # product = find_product_by_id(product_id)
    # if product:
    #     print("Product found:", product)
    
        # 4: Update the product

        # update_product_by_id(product_id, name='Ergonomic Gaming Chair', qty_in_stock=15)
        # print(f"Product with ID {product_id} updated successfully.")
        
        # 5: Delete the product

        # delete_product_by_id(product_id)
        # print(f"Product with ID {product_id} deleted successfully.")
    # else:
    #     print(f"No product found with ID {product_id}.")
