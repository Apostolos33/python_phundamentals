def positive(some_number: list) -> str:
    positive_numbers = [number for number in some_number if number >= 0]
    return f'Positive: {", ".join([str(number) for number in positive_numbers])}'
def negative(some_number: list) -> str:
    negative_numbers = [number for number in some_number if number < 0]
    return f'Negative: {", ".join([str(number) for number in negative_numbers])}'
def even(some_number: list) -> str:
    even_numbers = [number for number in some_number if number % 2 == 0]
    return f'Even: {", ".join([str(number) for number in even_numbers])}'
def odd(some_number: list) -> str:
    odd_numbers = [number for number in some_number if number % 2 != 0]
    return f'Odd: {", ".join([str(number) for number in odd_numbers])}'


numbers = [int(number) for number in (input().split(", "))]
print(positive(numbers))
print(negative(numbers))
print(even(numbers))
print(odd(numbers))
