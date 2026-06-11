def is_perfect_number(some_number: int) -> str:
    list_divisors = []
    for num in range(1, some_number):
        if some_number % num == 0:
            list_divisors.append(num) 
    if sum(list_divisors) == some_number:
        return "We have a perfect number!"
    return "It's not so perfect."

number = int(input())
result = is_perfect_number(number)
print(result)