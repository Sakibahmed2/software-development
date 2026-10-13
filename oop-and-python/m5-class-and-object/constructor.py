class Phone:
    name= "Honor"

    def __init__(self, owner, brand, price):
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self, phone, sms):
        text = f"Sending sms {phone} {sms}"
        print(text)

my_phone = Phone(owner="Sakib", brand="Honor", price=58000)
her_phone = Phone(owner="Nai", brand="Dont know", price=99999)

# print(my_phone.owner, my_phone.brand, my_phone.price)
# print(her_phone.owner, her_phone.brand, her_phone.price)


class Laptop:

    def __init__(self, name, price):
        self.name = name
        self.price = price

laptop1 = Laptop(name="MSI", price=93000)
laptop2 = Laptop(name="Acer", price=80000)

print(laptop1.name, laptop1.price)
print(laptop2.name, laptop2.price)
        