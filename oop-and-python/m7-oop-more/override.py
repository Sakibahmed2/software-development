class Person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("Vat dal")
    def exercise(self):
        raise NotImplementedError


class Cricketer(Person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
    # Override
    def eat(self):
        print("Vegetables")

    def exercise(self):
        print("Doing gym")

    # + sign operator overload
    def __add__(self, other):
        return self.age + other.age

    # * sign operator overload
    def __mul__(self, other):
        return self.height * other.height

sakib = Cricketer('Sakib', 22, 62, 73, 'BD')
taskin = Cricketer("Taskin", 38, 65, 80, "BD")
sakib.eat()
sakib.exercise()
print(sakib + taskin)
print(sakib * taskin)