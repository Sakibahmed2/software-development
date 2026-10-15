# base class, common class
class Gadget:
    def __init__(self, brand, price, color):
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
            return f'Running laptop {self.brand}'


class Laptop:
    def __init__(self, memory):
        self.memory = memory

   

    def codding(self):
        return f'Learning python and practicing'


class Phone(Gadget):
    def __init__(self, camera, brand, price, color):
        self.camera = camera
        super().__init__( brand, price, color)

   
    def call(self, number, text):
        return f'Sending sms to {number} text: {text}'

    def __repr__(self):
        return f'Phone: {self.brand}, {self.price}, {self.color}, {self.camera}'


# Inheritance
my_phone = Phone('20MP', 'Honor', 58000, 'Black')
print(my_phone)