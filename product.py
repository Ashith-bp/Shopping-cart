from db import get_connection

def list_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, price FROM products")
    for row in cursor.fetchall():
        print(f"{row[0]} - {row[1]} : ₹{row[2]}")
    conn.close()
