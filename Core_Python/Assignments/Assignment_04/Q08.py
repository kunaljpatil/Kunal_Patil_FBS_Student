# 8. WAP to find which numbers are divisible by 7 and multiple of 5 in a given range.
n1=int(input("Give starting number of range:"))
n2=int(input("Give ending number of range:"))

for i in range(n1,n2+1):
    if(i%7==0 and i%5==0):
        print(i)