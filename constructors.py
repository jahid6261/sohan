

class phon:
    manufactured='Bangladesh'

    def __init__(self,name,brand,price ):
        self.name=name
        self.brand=brand
        self.price=price
        

    def send_sms(self,phon,sms):
        text = f'sending to:{phon} {sms}'
        print(text)

my_phone = phon ('jahid','oppo',12000)
print(my_phone.name,my_phone.brand,my_phone.price)

my_phone.send_sms('01741006261','hell, i am coming')






