import re

pattern = r"^!([A-Z][a-z]{2,})!:\[([A-Za-z]{8,})\]$"

def is_valid_text(string:str)-> bool:
    if re.search(pattern, string):
        return True
    return False

number_of_texts = int(input())

for _ in range(number_of_texts):
    text = input()
    if is_valid_text(text):
        groups = re.search(pattern, text)
        command, sub_text = groups.group(1), groups.group(2)
        secret_message = []
        for char in sub_text:
            secret_message.append(str(ord(char)))
        print(f'{command}: {" ".join(secret_message)}')

    else:
        print("The message is invalid")
