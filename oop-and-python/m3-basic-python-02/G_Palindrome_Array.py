n = int(input())

nums = [int(x) for x in input().split()]


if nums == nums[::-1]:
    print("YES")
else:
    print('NO')