class Shop:
    shopping_mall= "jamuna"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []

    def add_to_cart(self, item):
        self.cart.append(item)


sakib = Shop("Sakib")
sakib.add_to_cart("Phone")
sakib.add_to_cart("Book")

print(sakib.cart)