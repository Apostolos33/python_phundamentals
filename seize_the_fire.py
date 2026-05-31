fires = input().split("#")
water = int(input())

total_efford = 0.0
total_fire = 0

print("Cells:")

for fire in fires:
    cells = fire.split(" = ")
    fire_type = cells[0]
    fire_value = int(cells[1])

    if (fire_type == "High") and (81 <= fire_value <= 125):
        if water >= fire_value:
            water -= fire_value
            total_fire += fire_value
            total_efford += fire_value * 0.25
            print(f" - {fire_value}")
        else:
            continue
    elif (fire_type == "Medium") and (51 <= fire_value <= 80):
        if water >= fire_value:
            water -= fire_value
            total_fire += fire_value
            total_efford += fire_value * 0.25
            print(f" - {fire_value}")
        else:
            continue
    elif (fire_type == "Low") and (1 <= fire_value <= 50):
        if water >= fire_value:
            water -= fire_value
            total_fire += fire_value
            total_efford += fire_value * 0.25
            print(f" - {fire_value}")
        else:
            continue
    else:
        continue

print(f"Effort: {total_efford:.2f}")
print(f"Total Fire: {total_fire}")

