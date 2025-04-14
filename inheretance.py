#based class,parent class, common class 


class Device:
    def __init__(self,brand ,price,color):
        self.brand=brand
        self.price=price
        self.color=color


    def run(self):
        return f'running laptop: {self.brand}'
    

class   laptop:
    def __init__(self,memory):
        self.memory=memory



class phon :
    def __init__(self,dual_sim):
        self.dual_sim=dual_sim


    def phone_call(self,number,text):
        return f'sending sms to:{number} with{text}'


class camra:
    def __init__(self,pixel):
        self.pixel=pixel
    def change_lens(self):
        pass    


    
              






    

