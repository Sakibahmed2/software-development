n = int(input())

a = list(map(int, input().split()))

counts = {}
for x in a:
    if x in counts:
        counts[x] += 1
    else:
        counts[x] = 1

removals = 0
for x in counts:
    freq = counts[x]
    if freq >= x:
        removals += freq - x
    else:
        removals += freq

print(removals)
