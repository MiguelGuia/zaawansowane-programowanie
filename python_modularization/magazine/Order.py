from python_modularization.magazine.utils import format_price

class Order:
    def __init__(self, order_id, products):
        self.order_id = order_id
        self.products = products

    def total_price(self):
        return sum(product.price for product in self.products)

    def __str__(self):
        products_str = "\n".join(str(product) for product in self.products)
        return (f"Order ID: {self.order_id}\n"
                f"Products:\n{products_str}\n"
                f"Total Price: {format_price(self.total_price())}")