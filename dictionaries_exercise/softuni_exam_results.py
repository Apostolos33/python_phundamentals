
exam_result_dictionary = {}
language_times = {}

command = input()

while command != "exam finished":
    command_as_list = command.split("-")
    if len(command_as_list) == 3:
        username, language, points = command_as_list
        points = int(points)
        if username not in exam_result_dictionary.keys():
            exam_result_dictionary[username] = [language, points]
            
        else:
            if exam_result_dictionary[username][0] == language:
                if exam_result_dictionary[username][1] < points:
                    exam_result_dictionary[username][1] = points
                
        if language not in language_times.keys():
            language_times[language] = 1

        else:
            language_times[language] += 1
        
        
        


    elif len(command_as_list) == 2:
        username = command_as_list[0]
        del exam_result_dictionary[username]


    command = input()

print("Results:")
for user_name, points in exam_result_dictionary.items():
    print(f"{user_name} | {points[1]}")

print("Submissions:")
for language, value in language_times.items():
    print(f"{language} - {value}")