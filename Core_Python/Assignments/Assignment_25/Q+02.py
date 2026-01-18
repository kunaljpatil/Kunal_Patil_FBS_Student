import re

def extract_dates(text):
    pattern = r"\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}|(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{1,2},\s\d{4}"
    return re.findall(pattern, text)

text = """
Meeting on 12/25/2023.
Holiday on 25-12-2023.
Project started on January 1, 2023.
"""

print(extract_dates(text))
