# Q6. Fibonacci series (n terms).

n = int(input("Enter A Number: "))

a = 0
b = 1
i = 1

while (i <= n):
    print(a, end = " ")
    nxt = a + b
    a = b
    b = nxt
    i = i + 1
