products = {}

while True:
    command = input()
    if command == "statistics":
        break

    key, value = command.split(": ")
    value = int(value)
    if key in products:
        products[key] += value
    else:
        products[key] = value

total_products = len(products)
total_quantity = sum(products.values())

print("Products in stock:")

for product, value in products.items():
    print(f"- {product}: {value}")

print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")