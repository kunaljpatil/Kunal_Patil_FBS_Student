# Q7. Find Intersection of Two Lists

lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]

inter = []

for x in lst1:
    for y in lst2:
        if x == y:
            inter = inter + [x]

print("Intersection =", inter)


