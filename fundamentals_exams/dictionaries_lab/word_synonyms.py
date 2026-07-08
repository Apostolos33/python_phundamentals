count_of_words = int(input())

words_and_synonyms = {}

for _ in range(count_of_words):
    word = input()
    synonym = input()
    if word in words_and_synonyms:
        words_and_synonyms[word].append(synonym)
    else:
        words_and_synonyms[word] = []
        words_and_synonyms[word].append(synonym)
    

for word in words_and_synonyms:
    print(f'{word} - {", ".join(words_and_synonyms[word])}')