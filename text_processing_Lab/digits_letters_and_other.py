all_the_letters = input()

numbers = ""
letters = ""
symbols = ""

for char in all_the_letters:
    if char.isdigit():
        numbers += char

    elif char.isalpha():
        letters += char
    
    else:
        symbols += char

print(numbers)
print(letters)
print(symbols)