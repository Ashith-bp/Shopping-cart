from db import get_connection

def add_to_cart(user_id, product_id, qty):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO cart(user_id, product_id, quantity) VALUES (%s,%s,%s)",
                   (user_id, product_id, qty))
    conn.commit()
    print("✅ Item added to cart!")
    conn.close()

def view_cart(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT p.name, p.price, c.quantity 
        FROM cart c JOIN products p ON c.product_id=p.id 
        WHERE c.user_id=%s
    """, (user_id,))
    total = 0
    for row in cursor.fetchall():
        item_total = row[1] * row[2]
        total += item_total
        print(f"{row[0]} x {row[2]} = ₹{item_total}")
    print(f"\nTotal = ₹{total}")
    conn.close()
