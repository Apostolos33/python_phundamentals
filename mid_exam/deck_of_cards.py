cards = input().split(", ")
number_of_commands = int(input())


for _ in range(number_of_commands):
    command = input()
    command_as_list = command.split(", ")
    action = command_as_list[0]

    if action == "Add":
        element = command_as_list[1]

        if element not in cards:
            cards.append(element)
            print("Card successfully added")
        else:
            print("Card is already in the deck")

    elif action == "Remove":
        element = command_as_list[1]

        if element in cards:
            cards.remove(element)
            print("Card successfully removed")
        else:
            print("Card not found")

    elif action == "Remove At":
        index = int(command_as_list[1])

        if index in range(len(cards)):
            cards.pop(index)
            print("Card successfully removed")
        else:
            print("Index out of range")

    elif action == "Insert":
        index = int(command_as_list[1])
        element = command_as_list[2]

        if index in range(len(cards)):
            if element not in cards:
                cards.insert(index, element)
                print("Card successfully added")
            else:
                print("Card is already added")

        else:
            print("Index out of range")

print(", ".join(cards))