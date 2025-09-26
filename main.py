from product import list_products
from cart import add_to_cart, view_cart

def main():
    user_id = 1  # fixed for now
    while True:
        print("\n=== Shopping Cart Menu ===")
        print("1. View Products")
        print("2. Add to Cart")
        print("3. View Cart")
        print("4. Exit")

        choice = input("Enter choice:")
        if choice == "1":
            list_products()
        elif choice == "2":
            pid = int(input("Enter Product ID: "))
            qty = int(input("Enter Quantity: "))
            add_to_cart(user_id, pid, qty)
        elif choice == "3":
            view_cart(user_id)
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
