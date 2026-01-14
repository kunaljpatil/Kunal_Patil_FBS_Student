# Q3. Write a program to find sum of following series using functions:
# (a) 1 + 2 + 3 + … + n


def f_num(num):
    sum = 0
    for i in range(1, num + 1):
        sum += i
    print(sum)

x = int(input("Enter Number: "))
f_num(x)
