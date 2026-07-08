characters = input().split(", ")

characters_dict = {character : ord(character) for character in characters}
print(characters_dict)
