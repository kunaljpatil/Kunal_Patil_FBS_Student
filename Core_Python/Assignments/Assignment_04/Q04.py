# 4. WAP to print factorial of a number .
n=int(input("Enter number whose factorial you want to ptint:"))
fact=1
for i in range(n,0,-1):
    fact=fact*i
print(f'The factorial of {n} = {fact}')    
    