number = input()
num_list = []

for num in number:
    num = int(num)
    num_list.append(num)

num_list.sort(reverse=True)

num_list = [str(num) for num in num_list]

print("".join(num_list))
