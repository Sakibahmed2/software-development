from food_item import FoodItem
from menu import Menu
from users import Customer, User, Admin, Employee
from restaurant import Restaurant
from orders import Order

mamar_restaurant = Restaurant("Mamar restaurant")

def customer_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    customer = Customer(name, phone, email, address)

    while True:
        print(f"Welcome {customer.name}")
        print("1. View Menu")
        print("2. Add item to cart")
        print("3. View cart")
        print("4. Pay bill")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            customer.view_menu(mamar_restaurant)
        elif choice == 2:
            item_name = input("Enter item name: ")
            item_quantity = int(input("Enter item quantity: "))
            customer.add_to_cart(mamar_restaurant, item_name, item_quantity)
        elif choice == 3:
            customer.view_cart()
        elif choice == 4:
            customer.pay_bill()
        elif choice == 5:
            break
        else:
            print("Invalid choice")




def admin_menu():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone: ")
    address = input("Enter your address: ")
    admin = Admin(name, phone, email, address)

    while True:
        print(f"Welcome {admin.name}")
        print("1. Add new item")
        print("2. Add new employee")
        print("3. View employee")
        print("4. View items")
        print("5. Delete item")
        print("6. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            item_name = input("Enter item name: ")
            item_price = int(input("Enter item price: "))
            item_quantity = int(input("Enter item quantity: "))
            item = FoodItem(item_name, item_price, item_quantity)
            admin.add_new_item(mamar_restaurant, item)
            
        elif choice == 2:
            name = input("Enter emp name: ")
            email = input("Enter emp email: ")
            phone = input("Enter emp phone: ")
            designation = input("Enter emp designation: ")
            age = int(input("Enter emp age: "))
            salary = input("Enter emp salary: ")
            address = input("Enter emp address: ")

            employee = Employee(name, phone, email, address, age, designation, salary)

            admin.add_emp(mamar_restaurant, employee)
            
        elif choice == 3:
            admin.view_emp(mamar_restaurant)

        elif choice == 4:
            admin.view_menu(mamar_restaurant)

        elif choice == 5:
            item_name = input("Enter item name to del: ")
            admin.delete_item(mamar_restaurant, item_name)

        elif choice == 6:
            break
        else:
            print("Invalid choice")


while True:
    print("Welcome!!")
    print("1. Customer")
    print("2. Admin")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        customer_menu()
    elif choice == 2:
        admin_menu()
    elif choice == 3:
        break
    else:
        print("Invalid choice input!!")