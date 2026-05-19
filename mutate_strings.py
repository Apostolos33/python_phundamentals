first_string = input()
secont_string = input()

mutated_string = ""

for index in range(len(first_string)):
    right_side = first_string[index + 1:]
    left_side = secont_string[:index + 1]
    mutated_string = left_side + right_side
    if first_string[index] != secont_string[index]:
        print(mutated_string)

