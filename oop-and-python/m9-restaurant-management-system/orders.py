
class Order:
    def __init__(self):
        self.items = {}

    def add_item(self, item, quantity):
        if quantity <= 0:
            print("Quantity must be greater than zero.")
        elif quantity > item.qty:
            print("Not enough items available.")
        else:
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity

            print("Item added to cart!")

    def rmv_item(self, item):
        if item in self.items:
            del self.items[item]

    @property
    def total_price(self):
        return sum(
            item.price * quantity
            for item, quantity in self.items.items()
        )

    def clear_cart(self):
        self.items = {}
