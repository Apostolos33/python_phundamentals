import re

pattern = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

full_name = input()

matches = re.findall(pattern, full_name)

print(" ".join(matches))