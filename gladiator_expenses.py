lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

helmet_broken_times = lost_fights_count // 2
sword_broken_times = lost_fights_count // 3
shield_broken_times = lost_fights_count // 6
armor_broken_times = shield_broken_times // 2

expenses = (helmet_broken_times * helmet_price) + (sword_broken_times * sword_price) + (shield_broken_times * shield_price) + (armor_broken_times * armor_price)

print(f"Gladiator expenses: {expenses:.2f} aureus")





    

