class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item" : item, "price": price, "quantity": quantity}
        self.cart.append(product)

    def remove_item(self, target):
        self.cart = [item for item in self.cart if item['item'] != target]

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item['price'] * item['quantity']

        if amount < total:
            print(f"Your total amount it {total} and you paid {amount} please provide {total-amount} more")
        else:
            extra = amount - total
            print(f"Here is your change after payment {extra}")



sakib = Shopping("Sakib Loskor")

sakib.add_to_cart('Alu', 50, 6)
sakib.add_to_cart('Dim', 20, 8)
sakib.add_to_cart('Rice', 50, 5)

print(sakib.cart)
sakib.remove_item('Alu')
print(sakib.cart)
# sakib.checkout(4400)