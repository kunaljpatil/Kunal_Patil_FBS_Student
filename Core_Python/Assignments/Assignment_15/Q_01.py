# Create a class Book with members as bid,bname,price and author.Add following
# methods:
# a. Constructor (Support both parameterized and parameterless)
# b. Destructor
# c. ShowBook

class Book:
    
    def __init__(self, bid=None, bname=None, price=None, author=None):
        self.bid = bid 
        self.bname = bname 
        self.price = price 
        self.author = author 
        
    def showBook(self):
        return f'Book Id: {self.bid}\nBook NAME: {self.bname}\nPRICE: {self.price}\nAUTHOR: {self.author}' 
        
    def __del__(self):
        print("The Program Is Closed!!!!!!!!!!")
        print()
        
b1 = Book(1234, "Pyhton", 500, "Ranjit Kamble")
b2 = Book()
print(b1.showBook())
del b1

print(b2.showBook())


