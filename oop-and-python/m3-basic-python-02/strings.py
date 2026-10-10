name = 'Sakib'
name2 = "Sakib"
name3 = """
    Hi im Sakib Ahmed Loskor
"""

print(name)
print(name2)
print(name3)

# String is a sequence of characters
for char in name2:
    print(char)

print(name2[3])
print(name2[1:6])
print(name2[-3])
print(name2[::1])

# name2[0] = 'R'
# print(name2)

print(name.upper())
print(name.lower())
print(name.capitalize())
# print(name.endswith())