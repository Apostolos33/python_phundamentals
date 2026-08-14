data = input().split()

command = input()
while command != "3:1":
    parts = command.split()
    action = parts[0]

    if action == "merge":
        start_index = int(parts[1])
        end_index = int(parts[2])

        # Clamp indexes to valid boundaries
        start_index = max(0, start_index)
        end_index = min(len(data) - 1, end_index)

        # Merge only if start_index is validly before end_index
        if start_index < end_index:
            merged_string = "".join(data[start_index : end_index + 1])
            data[start_index : end_index + 1] = [merged_string]

    elif action == "divide":
        index = int(parts[1])
        partitions = int(parts[2])

        target_str = data[index]
        part_len = len(target_str) // partitions

        new_parts = []
        for i in range(partitions):
            if i == partitions - 1:
                # The last partition gets all leftover characters
                new_parts.append(target_str[i * part_len :])
            else:
                new_parts.append(
                    target_str[i * part_len : (i + 1) * part_len]
                )

        # Replace the element at index with the divided pieces
        data[index : index + 1] = new_parts

    command = input()

print(data)






