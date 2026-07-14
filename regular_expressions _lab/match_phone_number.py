import re

patern = r'\+359 \d{1} \d{3} \d{4}\b|\+359-\d{1}-\d{3}-\d{4}\b'

tel_numbers = input()

match = re.findall(patern, tel_numbers)

print(", ".join(match))
