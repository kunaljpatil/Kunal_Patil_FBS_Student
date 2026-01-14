# 1. WAP to print all even numbers until n.
num = int(input("Enter num till you want to print even numbers: "))
i=1
while(i<=num):
    if(i%2==0):
        print(i)
    i=i+1
