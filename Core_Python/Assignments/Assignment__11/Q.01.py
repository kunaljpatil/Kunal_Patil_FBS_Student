# Q1. Put Even and Odd elements of a List into two Different Lists

lst = [10, 5, 7, 12, 3, 6]

even = []
odd = []

for x in lst:
    if x % 2 == 0:
        even = even + [x]
    else:
        odd = odd + [x]

print("Even List =", even)
print("Odd List =", odd)
