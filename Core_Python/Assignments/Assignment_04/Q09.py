# 9. WAP to print all numbers in a range divisible by a given number.
n1=int(input("Give starting number of range:"))
n2=int(input("Give ending number of range:"))
d=int(input("Enter a divisor:"))

for i in range(n1,n2+1):
    if(i%d==0):
        print(i)