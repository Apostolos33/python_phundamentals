gifts = input().split()


while True:
    command_line = input()
    if command_line == "No Money":
        break
    command = command_line.split()

    command_name = command[0]
    command_gift = command[1]
    if command_name == "Required":
        command_index = int(command[2])
        if 0 <= command_index < len(gifts):
            gifts[command_index] = command_gift
    elif command_name == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command_gift:
                gifts[i] = "None"
    elif command_name == "JustInCase":
        gifts.pop()
        gifts.append(command_gift)


while "None" in gifts:
    gifts.remove("None")

print(" ".join(gifts))