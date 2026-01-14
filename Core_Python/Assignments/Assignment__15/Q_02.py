# 2. Create a class Product with members as pid,pname,price and quantity .Add
# following methods:
# d. Constructor (Support both parameterized and parameterless)
# e. Destructor
# f. ShowBook

class Product:
    
    # Constructor: supports both parameterized and parameterless
    def __init__(self, pid=None, pname=None, price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price 
        self.quantity = quantity 
        
    # Method to show product details
    def ShowProduct(self):
        return (
            f'PRODUCT ID: {self.pid}\n'
            f'PRODUCT NAME: {self.pname}\n'
            f'PRICE: {self.price}\n'
            f'QUANTITY: {self.quantity}'
        )

    # Destructor
    def __del__(self):
        print(f'Destructor Called: Object with PID {self.pid} destroyed')
        

# Using parameterized constructor
p1 = Product(11001, 'Water Bottle', 100, 5)

# Using parameterless constructor
p2 = Product()

print(p1.ShowProduct())
# print()
del p1   # Explicit destructor call

print(p2.ShowProduct())
