import re

text = input()

pattern = r"\b_([A-Za-z0-9]+)\b"

find_all_names = re.findall(pattern, text)

print(",".join(find_all_names))