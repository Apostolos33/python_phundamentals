animals = input().split(", ")

wolf_index = animals.index("wolf")

sheep_pos = len(animals) - 1 - wolf_index

if sheep_pos == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_pos}! You are about to be eaten by a wolf!")



# animals = input().split(", ")

# for index, animal in enumerate(animals):
#     if animal == "wolf":
#         if index == len(animals) - 1:
#             print("Please go away and stop eating my sheep")
#         else:
#             sheep_position = len(animals[index + 1:])
#             print(f"Oi! Sheep number {sheep_position}! You are about to be eaten by a wolf!")