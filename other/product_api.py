from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# SQLite connection function
def db_connection():
    conn = sqlite3.connect('products_db.db')
    conn.row_factory = sqlite3.Row
    return conn

# Create the products table
def create_table():
    conn = db_connection()
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

@app.route('/products', methods=['GET'])
def get_all_products():
    conn = sqlite3.connect('products_db.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    
    if not products:
        return {"message": "No products found"}, 404
    
    return {
        "products": [{"id": p[0], "name": p[1], "barcode": p[2], "unit_price": p[3], "sell_price": p[4], "qty_in_stock": p[5]} for p in products]
    }, 200

# Save a new product
@app.route('/products', methods=['POST'])
def save_product():
    data = request.json
    name = data.get('name')
    barcode = data.get('barcode')
    unit_price = data.get('unit_price')
    sell_price = data.get('sell_price')
    qty_in_stock = data.get('qty_in_stock')

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO products (name, barcode, unit_price, sell_price, qty_in_stock)
        VALUES (?, ?, ?, ?, ?)
    ''', (name, barcode, unit_price, sell_price, qty_in_stock))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product saved successfully!'}), 201

# Find a product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def find_product(product_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id = ?', (product_id,))
    row = cursor.fetchone()
    conn.close()

    if row:
        product = dict(row)
        return jsonify(product), 200
    else:
        return jsonify({'error': 'Product not found'}), 404

# Update a product by ID
@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.json
    fields = ', '.join([f"{key} = ?" for key in data.keys()])
    values = list(data.values()) + [product_id]

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute(f'UPDATE products SET {fields} WHERE id = ?', values)
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product updated successfully!'}), 200

# Delete a product by ID
@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product deleted successfully!'}), 200

# Run the Flask app
if __name__ == '__main__':
    create_table()  # Create the table at application startup
    app.run(debug=True)
