list_words = input().split()
palindrom = input()
palindrom_list = [i for i in list_words if i == i[::-1]]
number_of_palindrom = palindrom_list.count(palindrom)
result = f"{palindrom_list}\nFound palindrome {number_of_palindrom} times"
print(result)