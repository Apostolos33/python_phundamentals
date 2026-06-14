first_words = input().split(", ")
secont_words = input().split(", ")
new_list = []
for word in first_words:
    for secont_word in secont_words:
        if word in secont_word:
            new_list.append(word)
            break

print(new_list)