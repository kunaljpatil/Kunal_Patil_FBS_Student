# Q1. Find elements in a given set that are not in another set.
s1 = {1, 2, 3, 4, 5}
s2 = {3, 4}

result = set()

for x in s1:
    if x not in s2:
        result.add(x)

print("Elements in s1 not in s2 =", result)
