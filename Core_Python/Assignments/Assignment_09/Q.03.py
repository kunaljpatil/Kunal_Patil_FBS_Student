# Q3. Write a program to reverse a given number using recursion.

def reverse(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        return reverse(n // 10, rev * 10 + digit)

num = int(input("Enter number: "))
print("Reversed number:", reverse(num))


