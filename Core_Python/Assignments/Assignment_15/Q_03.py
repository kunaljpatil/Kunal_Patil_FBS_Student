# 3. Create a class Shirt with members as sid,sname,type(formal etc), price and
# size(small,large etc) .Add following methods:
# g. Constructor (Support both parameterized and parameterless)
# h. Destructor
# i. ShowBook

class Shirt:
    
    def __init__(self, sid=0, sname=None, types=None, price=0, size=None):
        self.sid = sid
        self.sname = sname 
        self.types = types
        self.price = price
        self.size = size 
        
    def getData(self):
        return f'Shirt ID: {self.sid}\nShirt NAME: {self.sname}\nTypes: {self.types}\nPRICE: {self.price}\nSIZE: {self.size}'
        
    def __del__(self):
        print(f'The Given Shirt Data Is {self.sid} Destroyed!!!!')
        print("####################################################")
        print()
        
s1 = Shirt(10101, 'Raphal', 'Formal', 20000, 'Medium')
s2 = Shirt()

print(s1.getData())
del s1

print(s2.getData())
