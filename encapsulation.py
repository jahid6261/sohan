class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name=holder_name # public attribute
        self.branch='chiittagong' # protected
        self.__balance=initial_deposit # private


    def deposit(self,amount):
        self.__balance +=amount


    def get_balance(self):
        return self.__balance  

    def withdrow(self,amount):
        if amount <self.__balance:
            self.__balance=self.__balance-amount
            
            return amount
        else :
            return f'forkia taka nai'    
        


jahid = Bank('big brother',10000)


print(jahid.holder_name)
print(jahid.get_balance)
