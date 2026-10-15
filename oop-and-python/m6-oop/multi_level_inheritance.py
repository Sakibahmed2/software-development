class Vehicle:
    def __init__(self, name, price):
        self.name = name 
        self.price = price

    def move(self):
        pass

    def __repr__(self):
        return f'Name: {self.name}, Price: {self.price}'


class Bus(Vehicle):
    def __init__(self, name, price, seat):
        self.seat = seat
        return super().__init__(name, price)

    def __repr__(self):
        return super().__repr__()

class Truck(Vehicle):
    def __init__(self, name, price, weight):
        self.weight = weight
        return super().__init__(name, price)

class PickUpTruck(Truck):
    def __init__(self, name, price, weight):
        return super().__init__(name, price, weight)

class ACBus(Bus):
    def __init__(self, name, price, seat, temperature):
        self.temperature = temperature
        return super().__init__(name, price, seat)

    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()

green_line = ACBus('green', 5000, 50, 14)
print(green_line)