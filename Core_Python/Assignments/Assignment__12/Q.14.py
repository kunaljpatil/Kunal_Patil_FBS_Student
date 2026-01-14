# Q14. Count Occurrences of Each Word in a String

s = input("Enter string: ")

words = []
word = ""

# split manually
for ch in s:
    if ch != ' ':
        word = word + ch
    else:
        words = words + [word]
        word = ""

words = words + [word]  # last word

# count occurrences
for w in words:
    count = 0
    for x in words:
        if w == x:
            count = count + 1
    print(w, "=", count)
