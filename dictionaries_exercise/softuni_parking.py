registered_numbers_dictionary = {}

number_of_cars = int(input())

for car in range(number_of_cars):
    command = input().split()
    if len(command) == 2:
        name = command[1]
        if name not in registered_numbers_dictionary.keys():
            print(f"ERROR: user {name} not found")
        else:
            del registered_numbers_dictionary[name]
            print(f"{name} unregistered successfully")
    elif len(command) == 3:
        name, plate = command[1], command[2]
        if name in registered_numbers_dictionary.keys():
            print(f"ERROR: already registered with plate number {registered_numbers_dictionary[name]}")
        else:
            registered_numbers_dictionary[name] = plate
            print(f"{name} registered {plate} successfully")

for name, plate in registered_numbers_dictionary.items():
    print(f"{name} => {plate}")

