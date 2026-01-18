# Q8. Write a program to check whether a number is prime using recursion.

def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)

num = int(input("Enter number: "))
if is_prime(num):
    print(num, "is a Prime number")
else:
    print(num, "is Not a Prime number")


