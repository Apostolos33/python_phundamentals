current_event = input()
coffes_needed = 0

while current_event != "END":
    if current_event == "coding" or current_event == "dog" or current_event == "cat" or current_event == "movie":
        coffes_needed += 1
    elif current_event == "CODING" or current_event == "DOG" or current_event == "CAT" or current_event == "MOVIE":
        coffes_needed += 2

    current_event = input()

if coffes_needed > 5:
    print("You need extra sleep")

else:
    print(coffes_needed)

