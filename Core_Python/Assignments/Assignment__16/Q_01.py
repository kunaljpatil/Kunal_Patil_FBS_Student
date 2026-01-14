# 1. Create a class Book with members as bid,bname,price and author.Add following methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook
# d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0
    bid = 1100
    
    def __init__(self, bname='', price=0, author=''):
        Book.bid += 1
        self.bid = Book.bid 
        self.bname = bname 
        self.price = price 
        self.author = author 
        Book.count += 1 
        
    def showBook(self):
        return f'Book ID: {self.bid}\nBook_Name: {self.bname}\nPrice: {self.price}\nAUHTOR: {self.author}\nTOTAL BOOKS: {Book.count}'
        
    def __del__(self):
        print("Object Destroyed!!!!!!!!!!!!!!",self.bid)
        print()
        
b1 = Book('New_Java', 2000, 'Ranjit Kale')
print(b1.showBook())
del b1 

b2 = Book('New_Python', 1500, 'Ranjit Kamble')
print(b2.showBook())
del b2

# Parameterless constructor
b3 = Book()
print(b3.showBook())
del b3