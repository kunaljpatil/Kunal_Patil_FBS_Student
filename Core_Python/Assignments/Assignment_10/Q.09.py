# Q9. Read n elements and separate even and odd elements.

n = int(input("How many elements: "))

lst = []
even = []
odd = []

for i in range(n):
    num = int(input("Enter element: "))
    lst = lst + [num]

for x in lst:
    if x % 2 == 0:
        even = even + [x]
    else:
        odd = odd + [x]

print("Even List =", even)
print("Odd List =", odd)


