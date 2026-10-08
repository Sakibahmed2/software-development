numbers = [22, 43, 45, 65, 11, 88, 76, 45]

odds = []
even = []

for num in numbers:
    if num % 2 != 0:
        odds.append(num)
    else:
        even.append(num)

print(odds)
print(even)

odd_nums = [num for num in numbers if num % 2 != 0]
print(odd_nums)