numbers = input().split(", ")
number_of_beggars = int(input())
index = 0
int_numbers = []


for number in numbers:
    number = int(number)
    int_numbers.append(number)

beggars_sum_list = []

for beggar in range(number_of_beggars):
    beggar_sum = 0
    for number in int_numbers[index:len(int_numbers):number_of_beggars]:
        beggar_sum += number

    beggars_sum_list.append(beggar_sum)
    index += 1

print(beggars_sum_list)