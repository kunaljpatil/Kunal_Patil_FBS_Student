# Q11. Print all numbers divisible by m and n in the list.

lst = [10, 20, 30, 40, 50, 60]
m = int(input("Enter m: "))
n = int(input("Enter n: "))

for x in lst:
    if x % m == 0 and x % n == 0:
        print(x)

