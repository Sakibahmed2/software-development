balance = 5000

def buy_things(item, price):
    global balance # if want to update global variable than use global keyword
    balance = balance - (item * price)

buy_things(2, 1000)
print(balance)

