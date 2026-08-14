text = input()

command = input()

while command != "End":
    command_as_list = command.split()
    action = command_as_list[0]

    if action == "Translate":
        char, replacement = command_as_list[1], command_as_list[2]
        text = text.replace(char, replacement)
        print(text)

    elif action == "Includes":
        substring = command_as_list[1]
        if substring in text:
              print(True)
        else:
              print(False)

    elif action == "Start":
        substring = command_as_list[1]
        if substring in text[:len(substring)]:
            print(True)
        else:
            print(False)

    elif action == "Lowercase":
            text = text.lower()
            print(text)

    elif action == "FindIndex":
        character = command_as_list[1]
        index = len(text) -1 

        for char in text[-1::-1]:
            if char == character:
                break
            index -= 1

        print(index)

    elif action == "Remove":
        start_index, count = int(command_as_list[1]), int(command_as_list[2])
        text = text[:start_index] + text[start_index + count:]
        print(text)

    command = input()
