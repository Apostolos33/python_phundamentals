people_and_phone_numbers = {}

while True:
    command = input()
    if "-" not in command:
        number_of_people_to_search = int(command)
        break

    name, number = command.split("-")

    if name not in people_and_phone_numbers.keys():
        people_and_phone_numbers[name] = number
    else:
        people_and_phone_numbers[name] = number

for _ in range(number_of_people_to_search):
    search_contact = input()
    if search_contact not in people_and_phone_numbers.keys():
        print(f"Contact {search_contact} does not exist.")
    else:
        print(f"{search_contact} -> {people_and_phone_numbers[search_contact]}")

