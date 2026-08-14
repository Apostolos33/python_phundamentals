array_of_data = input().split()

command = input()

while command != "3:1":
    command_as_list = command.split()
    if command_as_list[0] == "merge":
        start_index, end_index = int(command_as_list[1]), int(command_as_list[2])
        if start_index in range(len(array_of_data)):
            if end_index in range(len(array_of_data)):
                for index in range(start_index, end_index + 1):
                    array_of_data[start_index] += array_of_data[index]
                for index in range(start_index +1, end_index + 1):
                    array_of_data[index] = "."
                array_of_data = [x for x in array_of_data if x != "."]
            else:
                for index in range(start_index + 1, len(array_of_data) - 1):
                    array_of_data[start_index] += array_of_data[index]
                for index in range(start_index + 1, len(array_of_data) -1):
                    array_of_data[index] = "."
                array_of_data = [x for x in array_of_data if x != "."]
        
    elif command_as_list[0] == "divide":
        index, partitions = int(command_as_list[1]), int(command_as_list[2])
        target = array_of_data[index]
        part_len = len(target) // partitions

        new_parts = []
        for i in range(partitions):
            if i == partitions - 1:
                new_parts.append(target[i * part_len:])
            else:
                new_parts.append(target[i * part_len : (i + 1) * part_len])

        array_of_data[index : index + 1] = new_parts



    command = input()

print(array_of_data)