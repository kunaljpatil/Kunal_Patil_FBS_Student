# 6. WAP to check if a given number is prime number or not.
n=int(input("Enter number to check whether its prime or not:"))
for i in range(2,n):
    if(n%i==0):
        print(f'{n} is not prime number')
        break
else:
    print(f'{n} its prime number')    