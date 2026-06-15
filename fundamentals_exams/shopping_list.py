list_of_groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    command_list = command.split()

    if not command_list:
        command = input()
        continue

    action = command_list[0]

    if action == "Urgent":
        item = command_list[1]

        if item not in list_of_groceries:
            list_of_groceries.insert(0, item)

    elif action == "Unnecessary":
        item = command_list[1]

        if item in list_of_groceries:
            list_of_groceries.remove(item)

    elif action == "Correct":
        old_item = command_list[1]
        new_item = command_list[2]

        if old_item in list_of_groceries:
            idx = list_of_groceries.index(old_item)
            list_of_groceries[idx] = new_item

    elif action == "Rearrange":
        item = command_list[1]

        if item in list_of_groceries:
            list_of_groceries.remove(item)
            list_of_groceries.append(item)
    command = input()

print(", ".join(list_of_groceries))