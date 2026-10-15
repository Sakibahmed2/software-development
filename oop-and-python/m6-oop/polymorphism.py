# poly -----> many (multiple)
# morph -----> shape

class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print('Animal making sound')


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("meow meow")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("gheu gheu")

class Goat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_sound(self):
        print("Siuuuuuuuuuuuuuu")

don = Cat('Real don')
don.make_sound()

shepard = Dog("Local shepard")
shepard.make_sound()

cr = Goat("C R")
cr.make_sound()

animals = [don, shepard, cr]

for animal in animals:
    animal.make_sound()