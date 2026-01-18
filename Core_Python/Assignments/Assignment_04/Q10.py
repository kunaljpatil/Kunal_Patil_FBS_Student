# 10. WAP to check if given number is Perfect Number.
n=int(input("Enter number to check whether its prefect or not: "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print(f'{n} is perfect number')    
else:
    print(f'{n} is not perfect number')        


