pokemons_string = input().split()
pokemons = [int(pokemon) for pokemon in pokemons_string]
pokemons_catched = []

while pokemons:
    index = int(input())

    if index < 0:
        pokemon_cathced = pokemons.pop(0)
        new_pokemom = pokemons[-1]
        pokemons.insert(0, new_pokemom)
    elif index >= len(pokemons):
        pokemon_cathced = pokemons.pop(-1)
        new_pokemom = pokemons[0]
        pokemons.append(new_pokemom)
    else:   
        pokemon_cathced = pokemons.pop(index)
        
    pokemons_catched.append(pokemon_cathced)
    for i in range(len(pokemons)):
        if pokemons[i] <= pokemon_cathced:
            pokemons[i] += pokemon_cathced
        elif pokemons[i] > pokemon_cathced:
            pokemons[i] -= pokemon_cathced
            

print(sum(pokemons_catched))




