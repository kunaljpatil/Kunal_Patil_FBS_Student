# Q9. Count Number of Words and Characters in a String

s = input("Enter string: ")

char_count = 0
word_count = 1   # words = spaces + 1

for ch in s:
    char_count = char_count + 1
    if ch == ' ':
        word_count = word_count + 1

print("Characters =", char_count)
print("Words =", word_count)
