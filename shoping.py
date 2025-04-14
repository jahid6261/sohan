
class shoping:
    def __init__(self,name):
        self.name=name

        self.cart=[]


    def     add_to_cart(self,item,price,quantity) :  
            product={'item':item,'price':price,'quantity':quantity}
            self.cart.append(product)                                             



    def checkout(self,amount):
         total = 0
         for item in self.cart:
           #print(item)
           total += item['price'] * item['quantity']
         print('total price', total)   


         if amount<total:
              print(f'pleade provide {total-amount} more')
         else :
              extra = amount - total
              print(f'here is your iems and extra money{extra}')      


jahid=shoping('jahid alam')
jahid.add_to_cart('potatu',50,6)
jahid.add_to_cart('Egg',12,24)
jahid.add_to_cart('rice',90,5)
print(jahid.cart)
jahid.checkout(1500)
