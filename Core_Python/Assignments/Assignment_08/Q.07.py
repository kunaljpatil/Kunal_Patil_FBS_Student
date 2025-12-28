# Q5. Sum of all prime numbers between 1 to n.

n = int(input("Enter a number: "))

for i in range(2, n):
    if n % i == 0:
        print("Not Prime", n)
        break
else:
    print("Prime", n)
