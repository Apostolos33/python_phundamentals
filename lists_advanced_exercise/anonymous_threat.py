strings = input().split()

command = input()

while command != "3:1":
    command_as_list = command.split()
    action = command_as_list[0]

    if action == "merge":
        startindex = int(command_as_list[1])
        endindex = int(command_as_list[2])
        startindex = max(0, startindex)
        endindex = min(len(strings) -1, endindex)

        if startindex < endindex:
            merged_string = "".join(strings[startindex : endindex + 1])
            strings[startindex : endindex + 1] = [merged_string]

    elif action == "divide":
        index = int(command_as_list[1])
        partitions = int(command_as_list[2])

        target_string = strings[index]
        len_partitions = len(target_string) // partitions

        new_list = []
        start = 0
        end = 1
        for i in range(partitions):
            if i == partitions - 1:
                new_list.append(target_string[i * len_partitions:])
                break
            new_list.append(target_string[start * len_partitions : end * len_partitions])
            start += 1
            end += 1
        strings[index : index + 1] = new_list

    command = input()

for string in strings:
    print(string, end=" ")