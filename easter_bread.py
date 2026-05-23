budget = float(input())
price_for_one_kg_flour = float(input())
colored_eggs = 0 

price_for_one_pack_of_eggs = price_for_one_kg_flour * 0.75
price_for_one_litter_milk = price_for_one_kg_flour * 1.25
price_for_250_ml_milk = price_for_one_litter_milk / 4
price_for_one_bread = price_for_one_kg_flour + price_for_one_pack_of_eggs + price_for_250_ml_milk

breads_we_can_make = budget // price_for_one_bread
budget_left = budget - (breads_we_can_make * price_for_one_bread)

for bread in range(1, int(breads_we_can_make + 1)):
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= bread - 2

print(f"You made {int(breads_we_can_make)} loaves of Easter bread! Now you have {int(colored_eggs)} eggs and {budget_left:.2f}BGN left.")

