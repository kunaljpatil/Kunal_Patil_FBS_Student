# 4. WAP to calculate area of triangle and rectangle  
print("Area Calculation")
Length =float(input("Enter the Length in cm :"))
Width =float(input("Enter the Width in cm :"))
Base =float(input("Enter the Base in cm :"))
Height =float(input("Enter the Height in cm :"))

AreaRectangle = Length * Width
AreaTriangle = (1/2)*Base*Height 

print(f'Area of Rectangle is {AreaRectangle}cm²')
print(f'Area of Triangle is {AreaTriangle}cm²')