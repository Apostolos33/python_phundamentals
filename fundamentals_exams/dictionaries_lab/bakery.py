foods_and_quantities = input().split()

bakery = {}

for index in range(0, len(foods_and_quantities), 2):
    key = foods_and_quantities[index]
    value = foods_and_quantities[index + 1]

    bakery[key] = int(value)

print(bakery)