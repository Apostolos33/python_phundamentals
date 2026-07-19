import re

command = input()

pattern = r">>([a-zA-Z]+)<<(\d+\.?\d+)!(\d+)"

names = []

total_price = 0

while command != "Purchase":
    matches = re.search(pattern, command)
    if matches:
        name = matches.group(1)
        price = matches.group(2)
        quantity = matches.group(3)
        names.append(name)
        total_price += float(price) * int(quantity)
    
    command = input()

print("Bought furniture:")
for name in names:
    print(name)

print(f"Total money spend: {total_price:.2f}")