import json
import csv

from product import Product


class Inventory:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.id in self.products:
            print("Product already exists in inventory.")
        else:
            self.products[product.id] = product
            print(f"Added {product.name} to inventory.")

    def remove_product(self, product_id):
        if product_id in self.products:
            removed = self.products.pop(product_id)
            print(f"Removed {removed.name} from inventory.")
        else:
            print("Product not found.")

    def update_quantity(self, product_id, amount):
        if product_id in self.products:
            self.products[product_id].quantity += amount
            print(f"Updated quantity: {self.products[product_id].quantity}")
        else:
            print("Product not found.")

    def display_inventory(self):
        if not self.products:
            print("Inventory is empty.")
        else:
            print("\n Current Inventory:")
            for product in self.products.values():
                print(product)
    
    def save_to_file(self, filename):
        data = {}
        for pid, product in self.products.items():
            data[pid] = {
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Inventory saved to file.")

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for pid, info in data.items():
                    self.products[pid] = Product(pid, info["name"], info["price"], info["quantity"])
            print("Inventory loaded from file.")
        except FileNotFoundError:
            print("No existing inventory file found. Starting fresh.")
            
    def search_product(self, keyword):
        found = []
        keyword_lower = keyword.lower()
        for product in self.products.values():
            if keyword_lower in product.name.lower() or keyword_lower == product.id.lower():
                found.append(product)

        if not found:
            print("No matching products found.")
        else:
            print("Search Results:")
            for product in found:
                print(product)
                
    def generate_report(self):
        if not self.products:
            print("Inventory is empty.")
            return

        total_value = 0
        highest = None
        lowest = None

        for product in self.products.values():
            value = product.price * product.quantity
            total_value += value

            if highest is None or value > highest[1]:
                highest = (product, value)
            if lowest is None or value < lowest[1]:
                lowest = (product, value)

        print("\nInventory Report:")
        print(f"Total Inventory Value: ${total_value:.2f}")
        print(f"Most Valuable Product: {highest[0].name} (${highest[1]:.2f})")
        print(f"Least Valuable Product: {lowest[0].name} (${lowest[1]:.2f})")
    
    def export_to_csv(self, filename):
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Write header
            writer.writerow(["Product ID", "Name", "Category", "Price", "Quantity", "Total Value"])
            # Write product rows
            for product in self.products.values():
                total_value = product.price * product.quantity
                writer.writerow([
                    product.id,
                    product.name,
                   #product.category,
                    f"{product.price:.2f}",
                    product.quantity,
                    f"{total_value:.2f}"
                ])
        print(f"Inventory exported to '{filename}' successfully.")



