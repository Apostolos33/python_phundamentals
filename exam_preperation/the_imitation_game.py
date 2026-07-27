encrypted_message = input()

command = input()

while command != "Decode":
    command_as_list = command.split("|")
    if command_as_list[0] == "Move":
       index = int(command_as_list[1])
       str_to_move = encrypted_message[:index]
       encrypted_message = encrypted_message[index:] + str_to_move

    elif command_as_list[0] == "Insert":
        index, value = int(command_as_list[1]), command_as_list[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]

    elif command_as_list[0] == "ChangeAll":
        char, new_char = command_as_list[1], command_as_list[2]
        encrypted_message = encrypted_message.replace(char, new_char)
            



    command = input()


print(f'The decrypted message is: {encrypted_message}')