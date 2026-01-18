# Q10. Write a program to reverse a number using recursion.

def rev_num(n, rev=0):
    if n == 0:
        return rev
    else:
        digit = n % 10
        return rev_num(n // 10, rev * 10 + digit)

num = int(input("Enter number: "))
print("Reversed Number =", rev_num(num))
