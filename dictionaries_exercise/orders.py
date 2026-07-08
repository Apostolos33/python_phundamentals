products_with_prices_and_quantity_dictionary = {}

while True:
    command = input().split()
    if len(command) == 1:
        break

    product, price, quantity = command
    price = float(price)
    quantity = int(quantity)

    if product not in products_with_prices_and_quantity_dictionary.keys():
        products_with_prices_and_quantity_dictionary[product] = []
        products_with_prices_and_quantity_dictionary[product].append(price)
        products_with_prices_and_quantity_dictionary[product].append(quantity)
    else:
        products_with_prices_and_quantity_dictionary[product][0] = price
        products_with_prices_and_quantity_dictionary[product][1] += quantity

for product, value in products_with_prices_and_quantity_dictionary.items():
    print(f"{product} -> {(value[0] * value[1]):.2f}")
