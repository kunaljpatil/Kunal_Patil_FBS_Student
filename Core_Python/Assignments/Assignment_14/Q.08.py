# Q8. Group all anagrams from a list.


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

groups = {}

for w in words:
    key = "".join(sorted(w))   # sorting creates same pattern

    if key not in groups:
        groups[key] = [w]
    else:
        groups[key].append(w)

print("Anagram Groups =")
for g in groups.values():
    print(g)
