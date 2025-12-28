# 4. Write a program to input all sides of a triangle and check whether triangle is valid or
# not.

a=int(input("Enter side a :"))
b=int(input("Enter side b :"))
c=int(input("Enter side c :"))

if((a+b>c) and (b+c>a) and (a+c>b)):
    print(f'its valid triangle because the sum of any two sides are greater than rest one according to Triangle Inequality Theorem')
else:
    print(f'Not valid triangle')    