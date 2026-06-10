def is_palindrome(numbers: list) -> bool:
    bool_list = []

    for num in numbers:
        left_side_list = []
        right_side_list = []
        lenght_of_num = len(num) // 2

        for index in range(len(num) -1,len(num) -1 - lenght_of_num, -1):
            digit = num[index]
            int_digit = int(digit)
            right_side_list.append(int_digit)

        for index in range(0, lenght_of_num):
            digit = num[index]
            int_digit = int(digit)
            left_side_list.append(int_digit)

        if left_side_list == right_side_list:
            bool_list.append(True)

        else:
            bool_list.append(False)


    for result in bool_list:
        print(result)





list_str_numbers = input().split(", ")
is_palindrome(list_str_numbers)


