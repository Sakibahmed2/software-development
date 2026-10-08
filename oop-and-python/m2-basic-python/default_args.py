def sum(a, b, c = 0):
    return a + b + c

# total = sum(10, 20)
total = sum(10, 20, 30)
print(total)


# args
def all_sum(*args):
    sum = 0
    for num in args:
        sum = sum + num
    return sum

all_total = all_sum(10, 20, 30, 40, 50)
print(all_total)