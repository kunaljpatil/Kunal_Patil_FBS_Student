# Q3. Write a program to find sum of following series using functions:

# (b) 1! + 2! + 3! + … + n!

n = int(input("Enter A Number"))
sum_fac = 0

for num in range(1, n + 1):
    fac_n = 1
    for j in range(1, num + 1):
        fac_n *= j
    sum_fac += fac_n

print(sum_fac)
