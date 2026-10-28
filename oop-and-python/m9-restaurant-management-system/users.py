from abc import ABC
from orders import Order
from food_item import FoodItem
from restaurant import Restaurant


class User(ABC):
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone 
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)
        self.cart = Order()

    def view_menu(self, restaurant):
        restaurant.menu.show_item()

    def add_to_cart(self, restaurant, item_name, quantity):
        item = restaurant.menu.find_item(item_name)
        if item:
            self.cart.add_item(item, quantity)
        else:
            print("Item not found!")

    def view_cart(self):
        print("\n*** View Cart ***")
        print("Name\tPrice\tQuantity")

        for item, quantity in self.cart.items.items():
            print(f"{item.name}\t{item.price}\t{quantity}")

        print("Total price:", self.cart.total_price)

    def pay_bill(self):
        print(f"Total {self.cart.total_price} paid successfully!")
        self.cart.clear_cart()


class Employee(User):
    def __init__(
        self, name, phone, email, address,
        age, designation, salary
    ):
        super().__init__(name, phone, email, address)
        self.age = age
        self.designation = designation
        self.salary = salary


class Admin(User):
    def __init__(self, name, phone, email, address):
        super().__init__(name, phone, email, address)

    def add_emp(self, restaurant, employee):
        restaurant.add_emp(employee)

    def view_menu(self, restaurant):
        restaurant.menu.show_item()

    def view_emp(self, restaurant):
        restaurant.view_emp()

    def add_new_item(self, restaurant, item):
        restaurant.menu.add_menu_item(item)

    def delete_item(self, restaurant, item_name):
        restaurant.menu.rmv_item(item_name)


# # Create food items
# fi = FoodItem("Pizza", 200, 20)
# fi2 = FoodItem("Burger", 100, 10)

# # Create restaurant and admin
# rs = Restaurant("Silver Spoon")
# admin = Admin("Sakib", 2211, "admin@gmail.com", "Dhaka")

# # Add food items
# admin.add_new_item(rs, fi)
# admin.add_new_item(rs, fi2)

# # Create customer
# customer1 = Customer(
#     "Sakib", 332111, "sakib@gmail.com", "Dhaka"
# )

# # View menu
# customer1.view_menu(rs)


# item_name = input("Enter item name: ")
# item_quantity = int(input("Enter item quantity: "))

# customer1.add_to_cart(rs,item_name, item_quantity)
# customer1.view_cart()