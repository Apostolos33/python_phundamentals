number_of_strings = int(input())
magic_word = input()

list_of_strings = []
special_strings = []


for _ in range(number_of_strings):
    current_string = input()
    list_of_strings.append(current_string)
    if magic_word in current_string:
        special_strings.append(current_string)



print(list_of_strings)
print(special_strings)
