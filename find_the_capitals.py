word = input()
index_list = []

for index, char in enumerate(word):
    if char.isupper():
        index_list.append(index)

print(index_list)
    



