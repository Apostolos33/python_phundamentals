string_numbers = input()
list_numbers = string_numbers.split()
oposite_list_numebrs = []

for number in list_numbers:
    oposite_number = int(number)
    oposite_list_numebrs.append(- oposite_number)

print(oposite_list_numebrs)

