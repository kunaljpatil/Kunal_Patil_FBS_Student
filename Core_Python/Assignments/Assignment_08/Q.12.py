# Q11. WAP to check if a given number is Armstrong or not.

n = int(input("Enter a number: "))

temp = n
sum = 0

while (temp > 0):
    dig = temp % 10
    sum = sum + (dig ** 3)
    temp = temp // 10

if(sum == n):
    print("the given number is ArmStrong")
else:
    print("the given number is not ArmStrong")
