version = [int(number) for number in input().split(".")]

for index in range(len(version) - 1, 0, -1):
    version[index] += 1
    if version[index] > 9:
        version[index] = 0
        version[index - 1] += 1
        if version[index - 1] > 9:
            version[index - 1] = 0
            version[index - 2] += 1
    
    break
print(*version, sep = ".")