class Product:
    def __init__(self, product_id, name, price, quantity):
        self.id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Price: ${self.price:.2f}, Quantity: {self.quantity}"
