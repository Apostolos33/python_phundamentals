import re

text = input()

patern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"
matches = re.finditer(patern, text)

for match in matches:
    print(match.group(), end=" ")