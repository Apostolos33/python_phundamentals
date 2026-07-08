words = input().split()

dictionery = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in dictionery:
        dictionery[word_lower] = 0
    
    dictionery[word_lower] += 1

for (key, value) in dictionery.items():
    if value % 2 != 0:
        print(key, end=" ")

