number_of_letters = int(input())

for first_symbol in range(97, 97 + number_of_letters):
    for secont_symbol in range(97, 97 + number_of_letters):
        for third_symbol in range(97, 97 + number_of_letters):

            print(f"{chr(first_symbol)}{chr(secont_symbol)}{chr(third_symbol)}")