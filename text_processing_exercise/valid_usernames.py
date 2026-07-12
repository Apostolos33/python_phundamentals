def lenght_is_valid(username: str) -> bool:
    if 3 <= len(username) <= 16:
        return True
    return False

def characters_are_valid(username: str) -> bool:
    for character in username:
        if not (character.isalnum() or character == "-" or character == "_"):
            return False
    return True

def symbols_are_valid(userame: str) -> bool:
    if " " in userame:
        return False
    return True

def user_name_is_valid(username: str) -> bool:
    if lenght_is_valid(username) and characters_are_valid(username) and symbols_are_valid(username):
        return True
    return False

usernames = input().split(", ")
for user_name in usernames:
    if user_name_is_valid(user_name):
        print(user_name)
