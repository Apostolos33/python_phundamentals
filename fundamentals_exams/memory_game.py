cards = input().split()
number_of_moves = 0
player_won_the_game = False
command = input()

while command != "end":
    number_of_moves += 1
    command_as_list = command.split()
    first_index = int(command_as_list[0])
    second_index = int(command_as_list[1])

    if first_index == second_index or first_index not in range(len(cards)) or second_index not in range(len(cards)):
        middle_of_cards = len(cards) // 2
        new_card = f"-{number_of_moves}a"
        cards.insert(middle_of_cards, new_card)
        cards.insert(middle_of_cards, new_card)
        print("Invalid input! Adding additional elements to the board")

    else:
        if cards[first_index] == cards[second_index]:
            element_to_remove = cards[first_index]
            print(f"Congrats! You have found matching elements - {element_to_remove}!")
            while element_to_remove in cards:
                cards.remove(element_to_remove)
        else:
            print("Try again!")

    if not cards:
        player_won_the_game = True
        break

    command = input()

if player_won_the_game:
    print(f"You have won in {number_of_moves} turns!")

else:
    print("Sorry you lose :(")
    print(" ".join(cards))    