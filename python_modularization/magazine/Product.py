from python_modularization.magazine.utils import format_price

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {format_price(self.price)}"