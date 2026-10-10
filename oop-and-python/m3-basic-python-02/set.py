# set: unique items collection. No duplicate
numbers = {12, 3, 32, 54, 38}
print(numbers)

numbers.add(22)
print(numbers)

numbers.remove(32)
print(numbers)

for item in numbers:
    print(item)

if 3 in numbers:
    print("Exist")
else:
    print("Not exist")

a = {1, 2, 3, 4, 5}
b = {1, 2, 3, 4, 5, 6, 7}
print(a & b)