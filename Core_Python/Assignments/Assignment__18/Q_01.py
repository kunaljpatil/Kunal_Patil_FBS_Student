
# 1. Create a class Complex Number with data members as real and imag and add following methods :
    # a. Constructor
    # b. Destructor
    # c. Overload +,- operator

class ComplexNumber:
     def __init__(self, real, imag):
         self.real = real
         self.imag = imag 
        
         
     def __add__(self, other):
         new_real = self.real + other.real
         new_imag = self.imag + other.imag
         return ComplexNumber(new_real, new_imag)
        
          
     def __sub__(self, other):
         new_real = self.real - other.real
         new_imag = self.imag - other.imag
         return ComplexNumber(new_real, new_imag)
      
     def __str__(self):
         return f"{self.real} + {self.imag}i"
         
         
     def __del__(self):
         print(f'The Given Object Is Destroyed!!!!!!')

# creating objects
c1 = ComplexNumber(10, 20)
c2 = ComplexNumber(5, 3)

# operations
print("C1 =", c1)
print("C2 =", c2)

c3 = c1 + c2
print("Addition:", c3)

c4 = c1 - c2
print("Subtraction:", c4)