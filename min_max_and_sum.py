def max_number(numbers: list) -> int:
    list_int_numbers = []
    for num in numbers:
        int_num = int(num)
        list_int_numbers.append(int_num)
    return max(list_int_numbers)


def min_number(numbers: list) -> int:
    list_int_numbers = []
    for num in numbers:
        int_num = int(num)
        list_int_numbers.append(int_num)
    return min(list_int_numbers)

def sum_numners(numbers: list) -> int:
    list_int_numbers = []
    for num in numbers:
        int_num = int(num)
        list_int_numbers.append(int_num)
    return sum(list_int_numbers)


def min_max_and_sum(numbers: list) -> int:
    result = ( f"The minimum number is {min_number(numbers)}\n"
              f"The maximum number is {max_number(numbers)}\n"
              f"The sum number is: {sum_numners(numbers)}"
              )
    return result

list_str_numbers = input().split()
final_result = min_max_and_sum(list_str_numbers)
print(final_result)


