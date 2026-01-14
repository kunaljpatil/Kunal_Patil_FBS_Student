# Q5. Find longest common prefix of all strings (using set).


lst = ["flower", "flow", "flight"]

prefix = ""

for i in range(len(lst[0])):
    s = set()
    for word in lst:
        s.add(word[i])

    if len(s) == 1:
        prefix = prefix + lst[0][i]
    else:
        break

print("Longest Common Prefix =", prefix)
