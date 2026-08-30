number_of_rows = int(input())

field = []

for r in range(number_of_rows):
    row_str = input()
    field.append(list(row_str))
    if "k" in row_str:
        start_row = r
        start_col = row_str.index("k")

rows = len(field)
cols = len(field[0]) if len(field) > 0 else 0 

visited = [[False] * cols for _ in range(rows)]

def moving(r, c, moves):
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return -1
    if field[r][c] == "#" or visited[r][c]:
        return -1
    
    visited[r][c] = True

    is_exit = (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)

    longest_path = moves if is_exit else - 1

    for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        path_len = moving(r + dr, c + dc, moves + 1)
        if path_len != -1:
            longest_path = max(longest_path, path_len)

    visited[r][c] = False

    return longest_path

max_moves = moving(start_row, start_col, 1)

if max_moves != -1:
    print(f"Kate got out in {max_moves} moves")
else:
    print(f"Kate cannot get out")