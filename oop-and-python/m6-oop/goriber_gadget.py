class Laptop:
    def __init__(self, brand, price, color, memory):
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running laptop {self.brand}'

    def codding(self):
        return f'Learning python and practicing'


class Phone:
    def __init__(self, brand, price, color, camera):
        self.brand = brand
        self.price = price
        self.color = color
        self.camera = camera

    def run(self):
        return f'Using phone'

    def call(self, number, text):
        return f'Sending sms to {number} text: {text}'

