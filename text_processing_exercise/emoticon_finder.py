text = input()

for index in range(len(text)):
    
    if text[index] == ":":
        if index < len(text) - 1:
            print(f"{text[index]}{text[index + 1]}")