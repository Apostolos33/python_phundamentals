number_of_messages = int(input())
message = ""

for _ in range (number_of_messages):
    number = int(input())

    if number == 88:
        message += "Hello\n"
    elif number == 86:
        message += "How are you?\n"
    elif number < 88:
        message += "GREAT!\n"
    else:
        message += "Bye.\n"
        
print(message)