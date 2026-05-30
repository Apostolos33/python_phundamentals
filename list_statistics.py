number_of_numbers = int(input())
list_negative_numbers = []
list_possitive_numbers = []

for _ in range(number_of_numbers):
    number = int(input())
    if number >= 0:
        list_possitive_numbers.append(number)
    else:
        list_negative_numbers.append(number)

print(f"""{list_possitive_numbers}
{list_negative_numbers}
Count of positives: {len(list_possitive_numbers)}
Sum of negatives: {sum(list_negative_numbers)}""")
