def sum_numbers(first: int, second: int) -> int:
    result = first + second
    return result

def subtract(first_num: int, second_num: int) -> int:
    second_result = first_num - second_num
    return second_result

def add_and_subtract(first_number: int, second_number: int, third_number: int) -> int:
    sum_of_numbers = sum_numbers(first_number, second_number)
    third_result = subtract(sum_of_numbers, third_number)
    return third_result


input_number_one = int(input())
input_number_two = int(input())
input_number_three = int(input())

final_result = add_and_subtract(input_number_one, input_number_two, input_number_three)
print(final_result)