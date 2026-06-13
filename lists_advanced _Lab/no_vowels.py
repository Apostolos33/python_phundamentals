string_input = input()

new_text = [i for i in string_input if i != "a" and i != "o" and i != "u" and i != "e" and i != "i" and i != "A" 
            and i != "O" and i != "U" and i != "E" and i != "I"
            ]

result = "".join(new_text)
print(result)