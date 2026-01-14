# 2. Create a class Product with members as pid,pname,price and quantity .Add following methods:
# e. Constructor (Support both parameterized and parameterless)
# f. Destructor
# g. ShowBook
# h. Add static member discount.
# i. Provide methods for applying discount on price of product.

class Product:
    
    discount = 0.30
    def __init__(self, pid=0, pname=None, price=0, quantity=0):
        self.pid = pid
        self.pname = pname
        self.price = price 
        self.quantity = quantity 
        # self.discount = Product.discount
        self.final_amt = 0
        
    def showBook(self):
            return f'PRODUCT-ID ; {self.pid}\nPRODUCT NAME: {self.pname}\nPRICE: {self.price}\nQuantity: {self.quantity}' 
        
    def applyDiscount(self):
        if self.pid == 0:
            print("Incomplete Details!!!!!!!!")
            return f'Fill The All Necessary Details About Product'
        else:
            self.final_amt = self.price - (self.price * Product.discount)
            data = f'Final Price Of {self.pname} : {self.final_amt}'  
            return data 
    
    def __del__(self):
        print(f'{self.pid} Object Is Destroyed!!!!!!!!')
        print("-------------------------------------------")
        print()
        
        
p1 = Product(111, 'Book', 2100, 2)
print(p1.showBook())
print(p1.applyDiscount())
del p1 

p2 = Product(121, 'NoteBook',3150, 2)
print(p2.showBook())
print(p2.applyDiscount())
del p2 

p3 = Product()
print(p3.showBook())
print(p3.applyDiscount())
del p3

        
        
        
        
        