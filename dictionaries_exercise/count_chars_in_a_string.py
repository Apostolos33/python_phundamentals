string = input()

chars_dictionery = {}

for char in string:
    if char == " ":
        continue
    if char not in chars_dictionery:
        chars_dictionery[char] = 0
        chars_dictionery[char] += 1

    else:
        chars_dictionery[char] += 1

for char, value in chars_dictionery.items():
    print(f"{char} -> {value}")



