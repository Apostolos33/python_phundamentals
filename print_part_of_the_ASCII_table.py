start = int(input())
end = int(input())

for number in range(start, end + 1):
    if number == end:
        print(chr(number))
    else:
        print(chr(number), end = " ")