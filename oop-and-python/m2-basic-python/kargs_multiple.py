def full_name(firsName, lastName):
    name = f'{firsName} {lastName}'
    return name

name = full_name("Sakib", "Ahmed")
print(name)


def famous_name(first, last, **addition):
    name = f'{first} {last} {addition['title']}'
    print(addition)
    for key, value in addition.items():
        print(key, value)
    return name

name = famous_name(first="Taheri", last="Gias", title="Hujur", addition="Sheikh")
print(name)


def a_lot(a, b):
    sum = a + b
    mul = a * b
    div = a - b
    # return [sum, mul, div] # list 
    return sum, mul, div #tuple 

print(a_lot(20, 20))