# Q8. Write a program to find reverse of a number.

n = int(input("Enter a number: "))

temp = n
sum = 0

while (temp > 0):
    dig = temp % 10
    sum = (sum * 10) + dig
    temp = temp // 10

print(sum)
