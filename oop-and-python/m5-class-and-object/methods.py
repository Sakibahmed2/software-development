class Phone:
    price = 50000
    color = 'black'
    features = ['camera', 'music']

    def call(self):
        print("Call a person")
    def send_sms(self,phone, sms):
        text = f'send sms to: {phone} and message {sms}'
        return text

my_phone = Phone()

print(my_phone.features)
my_phone.call()
result = my_phone.send_sms(4324, "I missed you")
print(result)