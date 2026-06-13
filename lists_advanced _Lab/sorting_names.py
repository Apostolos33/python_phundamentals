list_of_string = input().split(", ")
sorted_list = sorted(list_of_string, key=lambda x: (-len(x), x))
print(sorted_list)
