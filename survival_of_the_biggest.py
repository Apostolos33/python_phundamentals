string_numbers = input().split()
count_of_numbers_to_remove = int(input())

numbers = []

for num in string_numbers:
    num = int(num)
    numbers.append(num)

for num_remove in range(count_of_numbers_to_remove):
    smaller_number = 1000
    for number in numbers:
        if number < smaller_number:
            smaller_number = number
    
    numbers.remove(smaller_number)

str_numbers = [str(num) for num in numbers]

final_str_numbers = ", ".join(str_numbers)
print(final_str_numbers)

# numbers = [int(x) for x in input().split(" ")]
# numbers_to_remove = int(input())

# for _ in range(numbers_to_remove):
#     min_number = min(numbers)
#     numbers.remove(min_number)

# result = ",".join(str(num) for num in numbers)
# print(result)
