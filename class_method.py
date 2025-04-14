

class phon:
    brand='samsung'
    color= 'blu'
    price=12000
    features=['camra','speaker','hammer']

    def call(self):
        print('calling one person')

    def send_sms(self,phon,sms):
        text = f'sending sms to :{phon} and message:{sms}'
        return text    

my_phone=phon()   
print(my_phone.features)
my_phone.call()

result = my_phone.send_sms(23554,'tasfia i miss you')
print(result)