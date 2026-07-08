weapon_obtained = False

materials_and_quantities = {"shards": 0, "fragments": 0, "motes": 0}
Legendary_item = ""

while not weapon_obtained:
    command = input().split()
    for index in range(0, len(command), 2):
        quantity = int(command[index])
        material = command[index + 1].lower()
        
        if material in materials_and_quantities.keys():
            if material == "fragments":
                materials_and_quantities[material] += quantity
                if materials_and_quantities[material] >= 250:
                    materials_and_quantities[material] -= 250
                    Legendary_item = "Valanyr"
                    weapon_obtained = True
                    break
            elif material == "shards":
                materials_and_quantities[material] += quantity
                if materials_and_quantities[material] >= 250:
                    materials_and_quantities[material] -= 250
                    Legendary_item = "Shadowmourne"
                    weapon_obtained = True
                    break
            elif material == "motes":
                materials_and_quantities[material] += quantity
                if materials_and_quantities[material] >= 250:
                    materials_and_quantities[material] -= 250
                    Legendary_item = "Dragonwrath"
                    weapon_obtained = True
                    break

            else:
                materials_and_quantities[material] += quantity
        else:
            materials_and_quantities[material] = 0
            materials_and_quantities[material] += quantity
            
        

print(f"{Legendary_item} obtained!")
for material, quantity in materials_and_quantities.items():
    print(f"{material}: {quantity}")

    