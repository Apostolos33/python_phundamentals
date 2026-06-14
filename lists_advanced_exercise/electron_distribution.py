def filling_shels(some_number: int) -> list:
    shells = []
    shell = 0
    while some_number > 0:
        shell += 1
        electrons_per_shell_needed = 2 * (shell ** 2)
        if some_number >= electrons_per_shell_needed:
            shells.append(electrons_per_shell_needed)
        else:
            shells.append(some_number)

        some_number -= electrons_per_shell_needed
    return shells

number_of_electrons = int(input())
print(filling_shels(number_of_electrons))