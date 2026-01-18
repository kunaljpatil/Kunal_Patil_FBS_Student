import re

def censor(text, words):
    pattern = "|".join(words)
    return re.sub(pattern, "****", text)

    
text = "Python is easy and Python is powerful"
words = ["Python", "powerful"]

result = censor(text, words)
print(result)
