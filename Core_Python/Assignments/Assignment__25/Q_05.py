import re

def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))
    
print(is_valid_email("user@gmail.com"))     # True
print(is_valid_email("user123@domain.in")) # True
print(is_valid_email("user@.com"))         # False
print(is_valid_email("user@gmail"))        # False

