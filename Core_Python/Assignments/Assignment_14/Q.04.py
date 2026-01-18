# Q4. Find all pairs of elements in list whose sum equals a given value.



lst = [2, 4, 3, 5, 7, 8, 9]
target = 10

pairs = set()

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] + lst[j] == target:
            pairs.add((lst[i], lst[j]))

print("Pairs =", pairs)
