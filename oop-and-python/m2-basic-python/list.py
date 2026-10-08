# list, array, collection : same

# Index =  0   1   2   3   4
numbers = [10, 20, 30, 40, 50]
# Index =  -6  -4  -3  -2  -1

# list(start : end)
print(numbers[1: 3])

# list(start : end : steps)
print(numbers[0: 4: 2])
print(numbers[4: 0: -2])
print(numbers[2:])
print(numbers[:2])
print(numbers[:])
print(numbers[::-1])