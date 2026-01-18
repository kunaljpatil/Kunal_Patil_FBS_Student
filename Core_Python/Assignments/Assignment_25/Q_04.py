import re

def extract_urls(text):
    pattern = r"https?://\S+"
    return re.findall(pattern, text)
text = """
Visit https://www.google.com for search.
Check http://example.com for examples.
"""

print(extract_urls(text))
