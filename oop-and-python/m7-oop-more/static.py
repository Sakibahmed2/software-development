# static attribute (class attribute)
# static method @staticmethod
# class method @classmethod
# difference between class method and static method

class Shopping:
    cart = [] # class attribute # static attribute
    origin = "China"

    def __init__(self, location):
        self.name = "Jamuna"  # instance attribute
        self.location = "Jam er modde"

    def purchases(self, item, price, amount):
        remaining = amount - price
        print(f"Buying item {item}, price: {price} and remaining: {remaining}")

    @classmethod
    def dekhi(self, item):
        print("Just dekhi")

    @staticmethod
    def multiply( a, b):
        print(a * b)


bashundara = Shopping("Metro er niche")
bashundara.purchases("Lungi", 333, 444)

# Shopping().purchases('q', 2, 3)
Shopping.dekhi("Shampooo")
Shopping.multiply(5, 5)