class Calculator:
    brand = "Casio"

    def add(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


my_calc = Calculator()

sum = my_calc.add(10, 20)
sub = my_calc.sub(10, 5)
mul = my_calc.mul(5, 5)
div = my_calc.div(10, 2)

print("Sum: ", sum)
print("Sub: ", sub)
print("Mul: ", mul)
print("Div: ", div)