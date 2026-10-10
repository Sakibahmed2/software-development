person = {'name': "Sakib ahmed", 'address': "Dhaka", 'age': 22}
print(person)
print(person['age'])
print(person.keys())
print(person.values())

del person['age']
print(person)

for key, val in person.items():
    print("Key", key)
    print("Val", val)