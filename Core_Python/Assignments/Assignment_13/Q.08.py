# Q8. Python Program to Count Occurrences of Each Character in a String Using Dictionary


s = input("Enter string: ")

d = {}

for ch in s:
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] = d[ch] + 1

print("Character frequency =", d)
