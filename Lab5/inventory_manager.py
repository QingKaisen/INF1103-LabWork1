import os
import json

INVENTORY_FILE = "inventory.json"


def main():
    print("=========Welcome to the Inventory Management System=========")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = load_inventory(INVENTORY_FILE)

    print("----------- MENU -----------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Change Name/Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("----------------------------")

    while True:
        option = input("Enter option: ").strip()

        # 1. Display
        if option == "1":
            display_all(inventory)

        # 2. Add
        elif option == "2":
            print("Add New Product")
            product_id = input("Product ID: ").strip()
            if search_product(inventory, product_id) is not None:
                print(f"Error: Product ID {product_id} already exists.")
            else:
                name = input("Product Name: ").strip()
                try:
                    price = float(input("Price: $").strip())
                    stock = int(input("Stock Quantity: ").strip())
                except ValueError:
                    print("Error: Price must be a number and Stock Quantity must be a whole number.")
                else:
                    inventory = add_product(inventory, product_id, name, price, stock)
                    print("Product added successfully!")

        # 3. Update
        elif option == "3":
            print("Update Product")
            product_id = input("Enter Product ID: ").strip()
            product = search_product(inventory, product_id)
            if product:
                print("Product Found:")
                print(f"Name: {product['name']}")
                print(f"Current Stock: {product['stock']}")
 
                # Fix a typo in the name - leave blank to keep it as is
                name_input = input(f"New Name (press Enter to keep \"{product['name']}\"): ").strip()
                new_name = name_input if name_input != "" else None
 
                # Change stock - leave blank to keep it as is
                stock_input = input(f"New Stock Quantity (press Enter to keep {product['stock']}): ").strip()
                if stock_input == "":
                    new_stock = None
                else:
                    try:
                        new_stock = int(stock_input)
                    except ValueError:
                        print("Error: Stock Quantity must be a whole number. Stock left unchanged.")
                        new_stock = None
 
                if new_name is None and new_stock is None:
                    print("No changes made.")
                else:
                    inventory = update_stock(inventory, product_id, new_stock=new_stock, new_name=new_name)
                    print("Product updated successfully!")
            else:
                print("Product not found.")

        # 4. Search
        elif option == "4":
            print("Search Product")
            product_id = input("Enter Product ID: ").strip()
            product = search_product(inventory, product_id)
            if product:
                print("Product Found")
                print("-" * 50)
                print(f"ID: {product['id']}")
                print(f"Name: {product['name']}")
                print(f"Price: ${product['price']:.2f}")
                print(f"Stock: {product['stock']}")
                print("-" * 50)
            else:
                print("Product not found.")

        # 5. Save
        elif option == "5":
            print("Saving inventory...")
            save_inventory(INVENTORY_FILE, inventory)
            print(f"Inventory saved successfully to {INVENTORY_FILE}.")

        # 6. Exit
        elif option == "6":
            print("Saving inventory before exit...")
            save_inventory(INVENTORY_FILE, inventory)
            print("Inventory saved successfully.")
            print("Thank you for using Inventory Management System.")
            print("Program terminated.")
            break

        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()