def loading_bar(some_number: int) -> str:
    if some_number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    quantity_of_precent = some_number // 10
    quantity_of_dots = 10 - quantity_of_precent
    number_of_precent = "%" * quantity_of_precent
    number_of_dots = "." * quantity_of_dots
    return f"{some_number}% [{number_of_precent}{number_of_dots}]\nStill loading..."


    
number = int(input())
print(loading_bar(number))