cards = input().split()
count_of_faro_shuffles = int(input())


for shuffle in range(count_of_faro_shuffles):
    middle = len(cards) // 2
    left_side = cards[:middle]
    right_side = cards[middle:]
    shuffled_deck = []

    for index in range(len(left_side)):
        shuffled_deck.append(left_side[index])
        shuffled_deck.append(right_side[index])
    cards = shuffled_deck.copy()
        
    
print(cards)

