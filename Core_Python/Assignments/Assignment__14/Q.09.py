# Q9. Find all unique combinations of 3 numbers adding up to a target.




lst = [1, 2, 3, 4, 5, 6, 7]
target = 12

triplets = set()

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            if lst[i] + lst[j] + lst[k] == target:
                triplets.add((lst[i], lst[j], lst[k]))

print("Triplets =", triplets)
