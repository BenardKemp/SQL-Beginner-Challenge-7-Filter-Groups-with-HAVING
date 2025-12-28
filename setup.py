import sqlite3

conn = sqlite3.connect("example.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, " \
"name TEXT, " \
"category TEXT, " \
"price NUMBER, stock_qty INTEGER, created_at DATETIME)")


cursor.execute("INSERT INTO products (product_id, name, category, price, stock_qty, created_at) " \
" VALUES (101, 'Wireless Mouse', 'Accessories', 24.99, 120, '2025-01-10 09:00:00')")
cursor.execute("INSERT INTO products (product_id, name, category, price, stock_qty, created_at) " \
" VALUES (102, 'Mechanical Keyboard', 'Accessories', 89.00, 45, '2025-01-12 10:30:00')")
cursor.execute("INSERT INTO products (product_id, name, category, price, stock_qty, created_at) " \
" VALUES (103, '27-inch Monitor', 'Displays', 299.99, 18, '2025-01-15 12:20:00')")
cursor.execute("INSERT INTO products (product_id, name, category, price, stock_qty, created_at) " \
" VALUES (104, 'USB-C Hub', 'Accessories', 34.50, 70, '2025-01-18 14:00:00')")
cursor.execute("INSERT INTO products (product_id, name, category, price, stock_qty, created_at) " \
" VALUES (105, 'Laptop Stand', 'Workspace', 39.90, 32, '2025-01-21 16:10:00')")
conn.commit()
conn.close()