numbers = [int(number) for number in (input().split(", "))]
boundary = 0
while numbers:
    boundary += 10
    list_of_numbers = [number for number in numbers if number <= boundary]
    print(f"Group of {boundary}'s: {list_of_numbers}")
    numbers = [number for number in numbers if number not in list_of_numbers]

    