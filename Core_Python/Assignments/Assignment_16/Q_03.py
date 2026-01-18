# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and size(small,large etc) .Add following methods:
# j. Constructor (Support both parameterized and parameterless)
# k. Destructor
# l. ShowBook
# m. For each size of shirt price should change by 10%. (eg. If 1000 is price then small price = 1000, medium = 1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    
    size_ch_prize = 0.10
    sid = 11234001
    
    def __init__(self, sname='', stype='', price=0, size=''):
        self.sid = Shirt.sid 
        self.sname = sname 
        self.stype = stype
        self.price = price
        self.size = size 
        self.final_price = 0
        self.size_ch_prize = Shirt.size_ch_prize
        
        Shirt.sid += 1
        
    def showBook(self):
        return (
            f'SHIRT ID   : {self.sid}\n'
            f'SHIRT NAME : {self.sname}\n'
            f'SHIRT TYPE : {self.stype}\n'
            f'PRICE      : {self.price}\n'
            f'SIZE       : {self.size}'
        )
    
    def value(self):
        if self.size == 'small':
            self.size_ch_prize = 0.00
            self.final_price = (self.price * self.size_ch_prize) + self.price
        elif self.size == 'medium':
            self.size_ch_prize = 0.10
            self.final_price = (self.price * self.size_ch_prize) + self.price
        elif self.size == 'large':
            self.size_ch_prize = 0.20
            self.final_price = (self.price * self.size_ch_prize) + self.price
        elif self.size == 'xlarge':  
            self.size_ch_prize = 0.30
            self.final_price = (self.price * self.size_ch_prize) + self.price
        
        
        return f'The Final Price {self.sname} Shirt: {self.final_price}'
        
    def __del__(self):
        print(f'{self.sid} Object Is Destroyed!!!!!!!!')
        print("-------------------------------------------")
        print()
        
s1 = Shirt('Raphl', 'Casual', 1200, 'small')
print(s1.showBook())
print(s1.value())
del s1 
    
s2 = Shirt('Ameircan', 'Formal', 900, 'large')
print(s2.showBook())
print(s2.value())
del s2
        
s3 = Shirt('Russain', 'Suit', 6000, 'xlarge')
print(s3.showBook())
print(s3.value())
del s3

s4 = Shirt()
print(s4.showBook())
print(s4.value())
del s4
    
    
    
    
    
    
    
    