from locale import locale_encoding_alias
import re

# first part of email can have uppercase letters, lowercase letters and numbers
# then the email should have a domain
pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|edu|net)"

user_input = input()

if(re.search(pattern, user_input)):
    print("valid email")
else:
    print("invalid email")

