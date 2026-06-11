def calculate_factorial(some_number: int) -> int:
    final_number = 0
    for num in range(some_number - 1, 1 - 1, -1):
        factorial = some_number * num
        some_number = factorial
        final_number = factorial
    return final_number
    
def devide_factorials(number_one: int, number_two: int) -> int:
    first_number = calculate_factorial(number_one)
    second_number = calculate_factorial(number_two)
    result = first_number // second_number
    return result


number_one = int(input())
number_two = int(input())
result = devide_factorials(number_one, number_two)
print(f"{result:.2f}")
