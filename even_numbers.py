def is_even_number(numbers: list) -> list:
    even_numbers = []
    for num in numbers:
        number = int(num)
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
        
string_numbers = input().split()
result = is_even_number(string_numbers)
print(result)