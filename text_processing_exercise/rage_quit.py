string = input()
rage_string = ""

current_string = ""
times_to_write = ""


for index in range(len(string)):
    if not string[index].isdigit():
        current_string += string[index].upper()
    else:
        times_to_write += string[index]
        if index < len(string) - 1:
            if string[index + 1].isdigit():
                times_to_write += string[index + 1]
        rage_string += current_string * int(times_to_write)
        current_string = ""
        times_to_write = ""

   

        
print(f"Unique symbols used: {len(set(rage_string))}")
print(rage_string)