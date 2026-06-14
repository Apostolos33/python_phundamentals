product = input()
quantity = int(input())

def  calculate_total_price(product_type, quantity):
    if product_type == 'coffee':
        total_price = 1.50 * quantity
    elif product_type == 'coke':
        total_price = 1.40 * quantity
    elif product_type == 'water':
        total_price = 1.00 * quantity
    elif product_type == 'snacks':
        total_price = 2.00 * quantity
    return total_price

result = calculate_total_price(product, quantity)
print(f"{result:.2f}")