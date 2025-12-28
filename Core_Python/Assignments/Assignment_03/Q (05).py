# 5. Write a program to check whether the triangle is equilateral, isosceles or scalene
# triangle.
#Eqilateral--> all sides equal
#isosceles--> only 2 sides equal
#Scalene--> all sides different

a=int(input("Enter side a :"))
b=int(input("Enter side b :"))
c=int(input("Enter side c :"))

if(a==b==c):
    print(f'Its Equilateral Triangle')
elif((a==b) or (b==c) or (a==c)):
    print(f'Its isosceles Triangle')  
else:
    print(f'Triangle is Scalene with different sides')      