# Q3. Find all unique words and count frequency from list of strings using set.


lst = ["apple", "banana", "apple", "mango", "banana", "apple"]

unique = set()
for w in lst:
    unique.add(w)

for u in unique:
    count = 0
    for w in lst:
        if u == w:
            count = count + 1
    print(u, "=", count)
