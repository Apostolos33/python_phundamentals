
def characters_betwean_letters(first: str, second: str) -> str:
    list_of_chars = []
    for char in range(ord(first) + 1, ord(second)):
        list_of_chars.append(chr(char))
    return " ".join(list_of_chars)



first_letter = input()
second_letter = input()

result = characters_betwean_letters(first_letter, second_letter)
print(result)