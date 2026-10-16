class User:
    def __init__(self, name, age, money):
        self._name = name
        self._age = age
        self.__money = money

    # getter without any setter is readonly attribute
    @property
    def age(self):
        return self._age

    # getter
    @property
    def salary(self):
        return self.__money

    # setter
    @salary.setter
    def salary(self, value):
        if value < 0:
            print("Salary cannot be negative")
        self.__money += value

sakib = User("Sakib", 22, 13000)
# print(sakib.__money)
# print(sakib.age())
print(sakib.age)
print(sakib.salary)
sakib.salary = 2000
print(sakib.salary)