import math
import time

def timer(func):
    def inner(*args):
        print('Timer start')
        start = time.time()
        func(*args)
        print('Timer end')
        end = time.time()
        print(f"Total time taken: {end - start}")
    return inner

# timer()()

@timer
def get_factorial(n):
    print("Factorial staring")
    result = math.factorial(n)
    print(f'Factorial of {n} is: {result}')

get_factorial(1200)