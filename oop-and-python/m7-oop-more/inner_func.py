def double_decker():
    print("Starting the double decker")
    def inner_func():
        print("Inside the inner func")
        return 5000
    return inner_func

# print(double_decker())
print(double_decker()())


def do_something(work):
    print("Work started")
    work()
    print("Work ended")

def coding():
    print("Doing code")

print(do_something(coding))