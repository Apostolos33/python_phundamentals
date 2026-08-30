string = input()

numbers = [int(num) for num in string if num.isdigit()]
letters = [char for char in string if not char.isdigit()]
take_list = []
skip_list = []

for index in range(len(numbers)):
    if index % 2 == 0:
        take_list.append(numbers[index])
    else:
        skip_list.append(numbers[index])

letters_as_string = "".join(letters)
taken_string = ""
skiped_string = ""
for index in range(len(take_list)):
    characters_to_take = take_list[index]
    characters_to_skip = skip_list[index]
    taken_string += letters_as_string[:characters_to_take]
    letters_as_string = letters_as_string[characters_to_take:]
    skiped_string += letters_as_string[:skip_list[index]]
    letters_as_string = letters_as_string[skip_list[index]:]
    
print(taken_string)