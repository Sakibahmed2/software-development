from menu import Menu

class Restaurant:
    def __init__(self, name):
        self.name = name
        self.employees = []
        self.menu = Menu()

    def add_emp(self, employee):
        self.employees.append(employee)

    def view_emp(self):
        print("\nEmployee list")

        for emp in self.employees:
            print(emp.name, emp.phone, emp.email, emp.address)
