# Q7. Find missing numbers in second set compared to first, and vice-versa.


s1 = {1, 2, 3, 4, 5}
s2 = {2, 3, 6}

missing_in_s2 = set()
missing_in_s1 = set()

for x in s1:
    if x not in s2:
        missing_in_s2.add(x)

for x in s2:
    if x not in s1:
        missing_in_s1.add(x)

print("Missing in s2 =", missing_in_s2)
print("Missing in s1 =", missing_in_s1)
