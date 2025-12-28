# Q8. Create a duplicate of an existing list (not pointing to same list).

lst = [10, 20, 30, 40]
dup = []

for x in lst:
    dup = dup + [x]

print("Original List =", lst)
print("Duplicate List =", dup)


