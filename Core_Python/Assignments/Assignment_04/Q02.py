# 2. WAP to print all odd numbers until n.
num=int(input("Enter a num till you want to print odd numbers:"))
i=1
while(i<=num):
    if(i%2!=0):
        print(i)
    i+=1    