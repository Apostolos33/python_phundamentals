number_of_numbers = int(input())
list_of_numbers = []
filtred_list = []


for _ in range(number_of_numbers):
    current_number = int(input())
    list_of_numbers.append(current_number)

command = input()
if command == "even":
    for number in list_of_numbers:
        if number % 2 == 0:
            filtred_list.append(number)
elif command == "odd":
    for number in list_of_numbers:
        if number % 2 != 0:
            filtred_list.append(number)

elif command == "negative":
    for number in list_of_numbers:
        if number < 0:
            filtred_list.append(number)

elif command == "positive":
    for number in list_of_numbers:
        if number >= 0:
            filtred_list.append(number)

print(filtred_list)

