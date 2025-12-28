# Q2. Remove the intersection of a second set with the first set.

set1 = {1, 2, 3, 5, 4, 6, 9}
set2 = {2, 3, 8, 0, 1}

set3 = set()

for x in set1:
    if x not in set2:
        set3.add(x)

print(set3)
