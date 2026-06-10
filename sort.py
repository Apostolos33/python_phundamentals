def is_sorted_number(numbers: list) -> list:
    sorted_numbers = []
    for num in numbers:
        number = int(num)
        sorted_numbers.append(number)
    return sorted(sorted_numbers)
        
string_numbers = input().split()
result = is_sorted_number(string_numbers)
print(result)