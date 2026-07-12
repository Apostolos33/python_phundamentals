strings = input().split()

total_sum = 0

for string in strings:
    first_letter = string[0]
    last_letter = string[-1]
    number = int(string[1:-1])
    if first_letter.isupper():
        letter_position = ord(first_letter) - 64
        number = number / letter_position
    else:
        letter_position = ord(first_letter) - 96
        number = number * letter_position
    
    if last_letter.isupper():
        letter_position = ord(last_letter) - 64
        number -= letter_position
    else:
        letter_position = ord(last_letter) - 96
        number += letter_position
    total_sum += number

    

print(f"{total_sum:.2f}")