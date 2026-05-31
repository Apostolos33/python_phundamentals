factor = int(input())
count = int(input())
list_numbers = []

for index in range(1, count + 1):
    number = (index * factor)
    list_numbers.append(number)

print(list_numbers)