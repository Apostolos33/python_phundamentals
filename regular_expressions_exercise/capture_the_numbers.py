import re

pattern = r"\d+"
matches = []

text = input()
while text:
    find_all_numbers = re.findall(pattern, text)
    matches += find_all_numbers

    text = input()




print(" ".join(matches))