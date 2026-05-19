divisor = int(input())
largest_number = int(input())

for number in range(largest_number, 0, -1):
    if number % divisor == 0:
       print(number)
       break

