
num = input()

reversed_str = num[::-1]

reversed_num = int(reversed_str)
print(reversed_num)

if num == reversed_str:
    print("YES")
else:
    print("NO")
