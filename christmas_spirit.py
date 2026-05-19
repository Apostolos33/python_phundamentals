quantity = int(input())
days = int(input())
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
ornament_set_spirit = 5
tree_skirt_spirit = 3
tree_garland_spirit = 10 
tree_lights_spirit = 17

total_cost = 0
total_spirit = 0

for day in range(1, days + 1):
    if day % 11 == 0:
        quantity += 2 
    if day % 2 == 0:
        total_cost += quantity * ornament_set_price
        total_spirit += ornament_set_spirit
    if day % 3 == 0:
        total_cost += (quantity * tree_skirt_price )+ (quantity * tree_garland_price)
        total_spirit += tree_skirt_spirit + tree_garland_spirit

    if day % 5 == 0:
        total_cost += quantity * tree_lights_price
        total_spirit += tree_lights_spirit
    
    if day % 3 == 0 and day % 5 == 0:
        total_spirit += 30
    
    if day % 10 == 0:
        total_spirit -= 20
        total_cost += tree_garland_price + tree_lights_price + tree_skirt_price

if days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}\nTotal spirit: {total_spirit}")
    

