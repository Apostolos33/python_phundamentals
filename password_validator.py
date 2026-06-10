def check_lenght(some_password: str) -> str:
    if 6 <= len(some_password) <= 10:
        return None
    return "Password must be between 6 and 10 characters"

def check_characters(some_password: str) -> str:
    if some_password.isalnum():
        return None
    return "Password must consist only of letters and digits"

def check_digits(some_password: str) -> str:
    digits = 0

    for digit in some_password:
        if digit.isdigit():
            digits += 1
    if digits >= 2:
        return None
    return "Password must have at least 2 digits"

def is_password_valid(some_password: str) -> str:
    result = []
    result.append(check_lenght(some_password))
    result.append(check_characters(some_password))
    result.append(check_digits(some_password))
    while None in result:
        result.remove(None)
    if result == []:
        print("Password is valid")
    else:
        for error in result:
            print(error)




password = input()
is_password_valid(password)
