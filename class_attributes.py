

class shop:
    
    cart=[]
    shopping_mall='jamuna'
    def __init__(self,buyer):

        self.buyer=buyer

    def add_to_cart(self,item):
        self.cart.append(item)


jahid = shop('jah id')
jahid.add_to_cart('shoe')
jahid.add_to_cart('t shirt')    
print(jahid.cart)    


sajid= shop('sa jid')
sajid.add_to_cart('pen')
sajid.add_to_cart('book')
print(sajid.cart)  
            
    