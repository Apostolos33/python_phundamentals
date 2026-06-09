def sum_evens_and_odds_numbers(number: str) -> str:
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for num in number:
        int_num = int(num)
        if int_num % 2 == 0:
            sum_of_even_digits += int_num
        else:
            sum_of_odd_digits += int_num 
        
    return f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
    






input_number = input()
result = sum_evens_and_odds_numbers(input_number)
print(result)