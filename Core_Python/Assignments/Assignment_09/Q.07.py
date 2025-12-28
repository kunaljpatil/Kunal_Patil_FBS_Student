# Q7. Write a program to find sum of digits using recursion.

def sum_digits(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + sum_digits(n // 10)

num = int(input("Enter number: "))
print("Sum of digits =", sum_digits(num))


