text = input()
new_text = ""
strenght = 0
for index in range(len(text)):
    if text[index] == ">":
       new_text += ">"
       strenght += int(text[index  + 1])
    elif strenght > 0 and text[index] != ">":
        strenght -= 1
    else:
        new_text += text[index]
        
print(new_text)
