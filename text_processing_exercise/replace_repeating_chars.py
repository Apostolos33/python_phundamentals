text = input()
new_text = ""

for char in text:
    if not new_text or char != new_text[-1]:
        new_text += char

print(new_text)