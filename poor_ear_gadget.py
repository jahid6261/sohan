

class laptop:
    def __init__(self,brand,price,color,memory):
        self.brand=brand
        self.pricr=price
        self.color=color
        self.memory=memory
    def run(self) :
        return f'Running laptop: {self.brand}'   
    
    def coding(self):
        return f'learning python and practicing'
    

class phon:
    def __init__(self,brand,color,price,dula_sim):
        self.brand=brand
        self.color=color
        self.price=price
        self.dula_sim=dula_sim
    def run(self):
        return f'regurlay used to phon me'
    def phone_call(self,number,text):
        return f'sending sms to:{number} with {text}'
    

class camre:
    def __init__(self,brand,price,color,pixel):
        self.brand=brand
        self.price=price
        self.color=color
        self.pixel=pixel
    

    def run(self):
        pass
    def change_lens(self):
        pass
    


