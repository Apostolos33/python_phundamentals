crops = input().split(" & ")

command = input()

while command != "Collect!":
    command_as_list = command.split()
    action = command_as_list[0]

    if action == "Plant":
        element = command_as_list[1]
        if element not in crops:
            crops.insert(0, element)

    elif action == "Transplant":
        element = command_as_list[1]
        if element in crops:
            crops.remove(element)
            crops.append(element)

    elif action == "Replace":
        first_elemnt_index = int(command_as_list[1])
        second_elemt_index = int(command_as_list[2])
        if first_elemnt_index in range(len(crops)) and second_elemt_index in range(len(crops)):
            crops[first_elemnt_index], crops[second_elemt_index] = crops[second_elemt_index], crops[first_elemnt_index]

    elif action == "Uproot":
        element = command_as_list[1]
        while element in crops:
            crops.remove(element)

    command = input()

print(" | ".join(crops))