# Q4. Generate a Dictionary of Form (x : x*x) from 1 to n

n = int(input("Enter n: "))

d = {}

for x in range(1, n+1):
    d[x] = x * x

print("Generated Dictionary =", d)
