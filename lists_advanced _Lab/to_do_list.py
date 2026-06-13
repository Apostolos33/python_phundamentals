list = [0] * 10

while True:
    command = input().split("-")
    if command[0] == "End":
        break
    index = int(command[0]) - 1
    list.pop(index)
    list.insert(index, command[1])


result = [i for i in list if i != 0]
print(result)

