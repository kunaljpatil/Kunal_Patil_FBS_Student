# Q3. Write a program to find sum of following series using functions:

# (c) 1¹ + 2² + 3³ + … + nⁿ

n = int(input("Enter A Number"))
result = 0

for power in range(1, n + 1):
    result += (n ** power)

print(result)
