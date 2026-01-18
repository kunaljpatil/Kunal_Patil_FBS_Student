# 2. Create a class Distance with data members as km,m and cm and add following methods :
        # a. Constructor
        # b. Destructor
        # c. Overload +,- operator
 
class Distance:
    
    def __init__(self, km, m, cm):
        self.km = km 
        self.m = m 
        self.cm = cm
        
    def normalize(self):
        
        if self.cm >= 100:
            self.m = self.m + (self.cm // 100)
            self.cm = self.cm % 100
            
        if self.m >= 1000:
            self.km = self.km + (self.m // 1000)
            self.m = self.m % 1000
            
    def __add__(self, other):
        new_km = self.km + other.km
        new_m = self.m + other.m
        new_cm = self.cm + other.cm 
        
        result = Distance(new_km, new_m, new_cm)
        result.normalize()
        return result 
        
    def __sub__(self, other):
        new_km = self.km - other.km
        new_m = self.m - other.m
        new_cm = self.cm - other.cm
        
        if new_cm < 0:
            new_cm = new_cm + 100
            new_m = new_m - 1
            
        if new_m < 0:
            new_m = new_m + 1000
            new_km = new_km - 1
            
        result = Distance(new_km, new_m, new_cm)
        return result
    
    def __str__(self):
        return f'{self.km} KM {self.m} M {self.cm} CM'
        
    def __del__(self):
        print("--------------------------------------")
        
d1 = Distance(10, 200, 40)
d2 = Distance(5, 800, 80)

print('D1: ', d1)
print('D2: ', d2)

d3 = d1 + d2
print('D3: ', d3)

d4 = d1 - d2
print('D4: ', d4)