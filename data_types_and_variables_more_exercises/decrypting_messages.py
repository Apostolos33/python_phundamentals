key = int(input())

number_of_line = int(input())

message = ""

for _ in range(number_of_line):
    char = input()

    new_char = chr(ord(char) + key)
    message += new_char

print(message)
