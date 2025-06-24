from inventory import Inventory
from product import Product

def main():
    inventory = Inventory()

    while True:
        print("\n Inventory Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Quantity")
        print("4. Show Inventory")
        print("5. Search Product")
        print("6. Inventory Report")
        print("7. Export Inventory to CSV")
        print("8. Exit")


        choice = input("Choose an option (1–8): ")

        if choice == '1':
            pid = input("Enter product ID: ")
            name = input("Enter product name: ")
            try:
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
            except ValueError:
                print("Invalid input. Price must be a number and quantity must be an integer.")
                continue
            product = Product(pid, name, price, quantity)
            inventory.add_product(product)

        elif choice == '2':
            pid = input("Enter product ID to remove: ")
            inventory.remove_product(pid)

        elif choice == '3':
            pid = input("Enter product ID to update quantity: ")
            try:
                amount = int(input("Enter quantity to add/remove (use negative to reduce): "))
            except ValueError:
                print("Quantity must be an integer.")
                continue
            inventory.update_quantity(pid, amount)

        elif choice == '4':
            inventory.display_inventory()
        
        elif choice == '5':
            keyword = input("Enter product ID or name to search: ")
            inventory.search_product(keyword)
        
        elif choice == '6':
            inventory.generate_report()

        elif choice == '7':
            filename = input("Enter filename (e.g. inventory.csv): ")
            inventory.export_to_csv(filename)

        elif choice == '8':
            inventory.save_to_file("inventory.json")
            print("Exiting... Goodbye!")
            break


        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
