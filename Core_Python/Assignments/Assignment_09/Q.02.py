# Q2. Write a program to check if a number is Armstrong using recursion.

def armstrong(n, power):
    if n == 0:
        return 0
    else:
        digit = n % 10
        return (digit ** power) + armstrong(n // 10, power)

num = int(input("Enter number: "))
digits = len(str(num))

if armstrong(num, digits) == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
