import re

def word_count(text):
    words = re.findall(r"\w+", text.lower())
    
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    
    return freq
text = "Python is easy. Python is powerful!"

print(word_count(text))
