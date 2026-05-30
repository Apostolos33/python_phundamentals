number = input()
num_list = []

for num in number:
    num = int(num)
    num_list.append(num)

num_list.sort(reverse=True)

print(str(num_list))


