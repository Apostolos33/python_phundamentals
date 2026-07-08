string = input().split()
new_string = [word * len(word) for word in string]
print("".join(new_string))