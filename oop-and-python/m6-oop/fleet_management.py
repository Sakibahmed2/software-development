# Ena poribahan

class Company:
    def __init__(self, name, address):
        self.name = name
        self.bus = []
        self.routes = []
        self.drivers = []
        self.counter = []
        self.manager = []
        self.supervisors = []
        pass


class Driver:
    def __init__(self, name, license, age):
        self.license = license
        self.name = name
        self.age = age

class Counter:
    def __init__(self):
        pass
    def purchase_a_ticket(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

red_mia = Driver('Red mia', 'df232', 32)
