lst_of_numbers = input().split(", ")
even_number_indexes_list = []
for index in range(0, len(lst_of_numbers)):
    if int(lst_of_numbers[index]) % 2 == 0:
        even_number_indexes_list.append(index)

print(even_number_indexes_list)

