# 8. Write a program to solve the following series :
# a. 1! + 2! + 3! + 4! + .....n!
# b. N + N^2 + N^3+N^4 .....+N^N (here ^ means exponent)
# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.
# d. S = a + a2 / 2 + a3 / 3 + ...... + a10 / 10
# e. x - x2/3 + x3/5 - x4/7 + .... to n terms


# 8. Series Programs

# (a) 1! + 2! + 3! + ... + n!
n = int(input("Enter n for (a): "))
sum1 = 0
for i in range(1, n+1):
    fact = 1
    for j in range(1, i+1):
        fact *= j
    sum1 += fact
print("Sum of factorial series =", sum1)

# (b) N + N^2 + N^3 + ... + N^N
N = int(input("Enter N for (b): "))
sum2 = 0
for i in range(1, N+1):
    sum2 += N ** i
print("Sum of exponential series =", sum2)

# (c) Geometric series 1 + 2 + 4 + 8 + ... up to n terms
n = int(input("Enter n for (c): "))
sum3 = 0
term = 1
for i in range(n):
    sum3 += term
    term *= 2
print("Sum of geometric series =", sum3)

# (d) S = a + a^2/2 + a^3/3 + ... + a^10/10
a = int(input("Enter a for (d): "))
sum4 = 0
for i in range(1, 11):
    sum4 += (a ** i) / i
print("Sum of given series =", sum4)

# (e) x - x^2/3 + x^3/5 - x^4/7 + ... up to n terms
x = int(input("Enter x for (e): "))
n = int(input("Enter n for (e): "))
sum5 = 0
sign = 1
den = 1
for i in range(1, n+1):
    sum5 += sign * (x ** i) / den
    sign *= -1
    den += 2
print("Sum of alternating series =", sum5)
