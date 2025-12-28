# Write a program to input angles of a triangle and check whether triangle is valid or not.
ang1=int(input("Enter first angle: "))
ang2=int(input("Enter second angle: "))
ang3=int(input("Enter third angle: "))

sum=ang1+ang2+ang3

if(sum==180):
    print("Its Valid triangle")
else:
    print("Its not valid triangle")    