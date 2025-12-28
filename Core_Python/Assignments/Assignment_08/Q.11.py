# Q9. Write a program to check if entered number is a palindrome.

n = int(input("Enter a number: "))

temp = n
rev = 0

while (temp > 0):
    dig = temp % 10
    rev = rev * 10 + dig
    temp = temp // 10

if rev == n:
    print("Palindrome")
else:
    print("Not Palindrome")
