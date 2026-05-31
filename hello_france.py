items_with_their_prices= input().split("|")
budget = float(input())
initial_budget = budget
ticked_for_france = 150 
sold_items_money = 0.0

for i in items_with_their_prices:
    items_prices = i.split("->")
    item = items_prices[0]
    price = float(items_prices[1])
    if item == "Clothes" and price <= 50.00:
        if budget >= price:
            budget -= price
            sold_items_money += price * 1.40
            print(f"{(price * 1.4):.2f}", end= " ")
    elif item == "Shoes" and price <= 35.00:
        if budget >= price:
            budget -= price
            sold_items_money += price * 1.40
            print(f"{(price * 1.4):.2f}", end= " ")
    
    elif item == "Accessories" and price <= 20.50:
        if budget >= price:
            budget -= price
            sold_items_money += price * 1.40
            print(f"{(price * 1.4):.2f}", end= " ")
    else:
        continue
print()
print(f"Profit: {((sold_items_money + budget) - initial_budget):.2f}")

if (sold_items_money + budget) >= ticked_for_france:
    print("Hello, France!")
else:
    print("Not enough money.")


