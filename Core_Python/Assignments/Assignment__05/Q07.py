# 7. Write a program to print first n prime numbers.
n=int(input("Enter n value till you want to print prime numbers : "))
for i in range(2,n+1):
    for j in range(2,i):
        if(i%j==0):
            break
    else:
        print(f'{i}')