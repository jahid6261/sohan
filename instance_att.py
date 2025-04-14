

class shop:

    shopping_mall='jamuna'

    def __init__(self,buyer):
        self.buyer=buyer
        self.cart=[]
    def add_to_cart(self,item):
            self.cart.append(item)

jahid = shop('ja hi d')
jahid.add_to_cart('shoes')
jahid.add_to_cart('pent')
print(jahid.cart)


sajid =shop("sa ji")
sajid.add_to_cart('pen')
sajid.add_to_cart('book')
print(sajid.cart)


sakib =shop("kinbe")
sakib.add_to_cart('t-shirt')
sakib.add_to_cart('panjabi')
print(sakib.cart)

            
    
