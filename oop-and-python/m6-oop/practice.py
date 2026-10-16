class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Shop:
    def __init__(self, shop_name):
        self.shop_name = shop_name
        self.products = [] 

    def add_product(self, product):
        self.products.append(product)
        print(f"Product '{product.name}' added successfully!!")

    def buy_product(self, product_name):
        for item in self.products:
            if item.name.lower() == product_name.lower():
                if item.quantity > 0:
                    item.quantity -= 1
                    print(f"Congrats! You bought the {item.name}.")
                    return  
                else:
                    print(f"Sorry, {item.name} is out of stock.")
                    return
        
        print("Product not available.")


sakib_shop = Shop("Sakib's Tech Store")

mobile = Product('Mobile', 30000, 2)
laptop = Product('Laptop', 80000, 1)

sakib_shop.add_product(mobile)
sakib_shop.add_product(laptop)

sakib_shop.buy_product('laptop')
