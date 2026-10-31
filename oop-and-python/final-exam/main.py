from bus import BusSystem
from user import Admin


def admin_menu(bus_system):
    while True:
        print("\n========== Admin Menu ==========")
        print("1. Add Bus")
        print("2. View All Buses")
        print("3. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            number = input("Enter bus number: ")
            route = input("Enter bus route: ")
            seats = int(input("Enter total seats: "))
            bus_system.add_bus(number, route, seats)
            
        elif choice == "2":
            bus_system.show_buses()

        elif choice == "3":
            print("Admin logged out successfully.")
            break

        else:
            print("Invalid choice. Please select 1, 2, or 3.")



bus_system = BusSystem()
admin = Admin("admin", "1234")

bus_system.add_bus("101", "Dhaka to Chittagong", 3)
bus_system.add_bus("102", "Dhaka to Sylhet", 2)
bus_system.add_bus("103", "Dhaka to Cox's Bazar", 4)

while True:
    print("\n====== Bangladesh Bus Ticket Booking System ======")
    print("1. Admin Login")
    print("2. Book Ticket")
    print("3. View Buses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")

        if admin.login(username, password):
            print("Login successful!")
            admin_menu(bus_system)
        else:
            print("Invalid username or password.")

    elif choice == "2":
        bus_system.show_buses()

        bus_number = input("Enter bus number: ")
        name = input("Enter passenger name: ")
        phone = input("Enter phone number: ")

        if name.strip() == "" or phone.strip() == "":
            print("Name and phone cannot be empty.")
        else:
            bus_system.book_ticket(bus_number, name, phone)

    elif choice == "3":
        bus_system.show_buses()

    elif choice == "4":
        print("Thank you for using the Bus Ticket Booking System.")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

