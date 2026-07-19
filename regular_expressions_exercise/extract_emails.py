import re

text = input()

pattern = pattern = r"\s[a-z0-9]+(?:[\.\-_][a-z0-9]+)*@[a-z]+(?:-[a-z]+)*(?:\.[a-z]+(?:-[a-z]+)*)+\b"

matches = re.findall(pattern, text)

for email in matches:
    print(email)