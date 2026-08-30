number_of_rows = int(input())

field = []

for _ in range(number_of_rows):
    row = list(map(int, input().split()))
    field.append(row)


attacks = input().split()

destroyed_ships = 0

for attack in attacks:
    row, col = map(int, attack.split("-"))

    if field[row][col] > 0:
        field[row][col] -= 1
        if field[row][col] == 0:
            destroyed_ships += 1

print(destroyed_ships)