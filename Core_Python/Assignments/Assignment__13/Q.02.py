# Q2. Python Program to Concatenate Two Dictionaries Into One

d1 = {1: "a", 2: "b"}
d2 = {3: "c", 4: "d"}

d3 = {}

# copy d1
for k in d1:
    d3[k] = d1[k]

# copy d2
for k in d2:
    d3[k] = d2[k]

print("Merged Dictionary =", d3)
