# Q10. Print list after removing even numbers

lst = [1, 2, 3, 4, 5, 6, 7]
new = []

for x in lst:
    if x % 2 != 0:
        new = new + [x]

print("List after removing even numbers =", new)
