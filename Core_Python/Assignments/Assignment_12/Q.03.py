# Q3. Detect if Two Strings are Anagrams

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# convert both strings to lists
l1, l2 = [], []

for x in s1:
    l1 = l1 + [x]

for x in s2:
    l2 = l2 + [x]

# bubble sort both lists
for i in range(len(l1)):
    for j in range(len(l1)-1):
        if l1[j] > l1[j+1]:
            l1[j], l1[j+1] = l1[j+1], l1[j]

for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j] > l2[j+1]:
            l2[j], l2[j+1] = l2[j+1], l2[j]

if l1 == l2:
    print("Strings are Anagrams")
else:
    print("Not Anagrams")
