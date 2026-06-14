secret_message = input().split()
print(secret_message) 

for message in secret_message:
    message = list(message)
    new_message = []
    digits_as_string = ""
    for index in range(len(message)):
        if message[index].isdigit():
            digits_as_string += message[index]
        else:
            break
    first_letter = chr(int(digits_as_string))
    new_message += [first_letter] + message[index::]
    new_message[1], new_message[-1] = new_message[-1], new_message[1]
    print("".join(new_message), end=" ")


    
