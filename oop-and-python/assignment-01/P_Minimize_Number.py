n = int(input())

a = list(map(int, input().split()))

min_operations = 35

for x in a:
    count = 0
    while x % 2 == 0:
        count += 1
        x //= 2
    
    if count < min_operations:
        min_operations = count

print(min_operations)
