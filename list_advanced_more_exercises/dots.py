number_of_rows = int(input())

field = []

for _ in range(number_of_rows):
    row = input().split()
    field.append(row)

rows = len(field)
cols = len(field[0]) if rows > 0 else 0

visited = [[False for _ in range(cols)] for _ in range(rows)]

def flood(r, c):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return 0 

    if field[r][c] != "." or visited[r][c]:
        return 0  

    visited[r][c] = True

    count = 1

    count += flood(r - 1, c)
    count += flood(r + 1, c)
    count += flood(r, c - 1)
    count += flood(r, c + 1)

    return count

maxcount = 0

for r in range(rows):
    for c in range(cols):
        if field[r][c] == "." and not visited[r][c]:
            current_count = flood(r, c)
            maxcount = max(maxcount, current_count)

print(maxcount)
