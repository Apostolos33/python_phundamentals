water_tank = 255
number_of_pours = int(input())

for pour in range(number_of_pours):
    current_pour = int(input())
    if water_tank < current_pour:
        print("Insufficient capacity!")
        continue
    
    water_tank -= current_pour

print(255 - water_tank)
