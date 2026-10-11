s = input()

balance = 0
count = 0
start_index = 0
substrings = []

for i, char in enumerate(s):
    if char == 'L':
        balance += 1
    else: 
        balance -= 1   
    if balance == 0:
        count += 1
        substrings.append(s[start_index:i+1])
        start_index = i + 1

print(count)

for sub in substrings:
    print(sub)
