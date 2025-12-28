# Q7. Write a program to find sum of digits of a number using function.

n = int(input("Enter the Number: "))
temp = n
t_d = int(input("Enter the How many digits in Number: "))
sum = 0

for i in range(1, t_d + 1):
    dig = temp % 10
    sum += (dig ** t_d)
    temp = temp // 10

print(sum)


