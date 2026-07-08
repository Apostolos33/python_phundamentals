products_and_quantities = input().split()

products = {}

for index in range(0, len(products_and_quantities), 2):
    key = products_and_quantities[index]
    value = int(products_and_quantities[index + 1])

    products[key] = value

products_to_search = input().split()

for product in products_to_search:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")


