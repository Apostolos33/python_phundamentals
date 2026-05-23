number_of_snowballs = int(input())
highest_snowball_value = 0
result = ""

for snowball in range(number_of_snowballs):
    weight_of_the_snowball = int(input())
    time_needed = int(input())
    quality = int(input())

    snowball_value = (weight_of_the_snowball // time_needed) ** quality
    if snowball_value > highest_snowball_value:
        highest_snowball_value = snowball_value
        result = f"{weight_of_the_snowball} : {time_needed} = {snowball_value} ({quality})"

print(result)