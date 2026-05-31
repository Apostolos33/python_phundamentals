events = input().split("|")
total_energy = 100
total_coins = 100
all_tasks_completed = True

for event in events:
    event_values = event.split("-")
    event_name, event_value = event_values[0], int(event_values[1])

    if event_name == "rest":
        initial_energy = total_energy
        total_energy += event_value
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - initial_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif event_name == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_value
            print(f"You earned {event_value} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
            continue
    else:
        if total_coins >= event_value:
            total_coins -= event_value
            print(f"You bought {event_name}.")   
        else:
            print(f"Closed! Cannot afford {event_name}.")
            all_tasks_completed = False
            break

if all_tasks_completed:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
