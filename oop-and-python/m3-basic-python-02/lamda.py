doubled = lambda num : num * 2

result = doubled(22)
# print(result)


numbers = [12, 3, 32, 54, 38]

doubled_num = map(lambda x : x * 2, numbers)
print(list(doubled_num))


actors = [
    {'name': 'srk','age': 43},
    {'name': 'salman','age': 44},
    {'name': 'amir', 'age': 42},
    {'name': 'sid', 'age': 34}
]

juniors = filter(lambda actor : actor['age'] < 40, actors)
print(list(juniors))