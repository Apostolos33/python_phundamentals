string_numbers = input().split()

rounded_numbers = [round(float(num)) for num in string_numbers]
print(rounded_numbers)