lessons = input().split(", ")

command = input()

while command != "course start":
    command_as_list = command.split(":")
    action, lesson = command_as_list[0], command_as_list[1]

    if action == "Add":
        if lesson not in lessons:
            lessons.append(lesson)

    elif action == "Insert":
        index = int(command_as_list[2])
        if lesson not in lessons:
            lessons.insert(index, lesson)

    elif action == "Remove":
        exercise = f"{lesson}-Exercise"
        if lesson in lessons:
            lessons.remove(lesson)
        if exercise in lessons:
            lessons.remove(exercise)
        

    elif action == "Swap":
        exercise = f"{lesson}-Exercise"
        second_lesson = command_as_list[2]
        if lesson in lessons and second_lesson in lessons:
            index_one = lessons.index(lesson)
            index_two = lessons.index(second_lesson)
            ex1, ex2 = f"{lesson}-Exercise", f"{second_lesson}-Exercise"
            lessons[index_one], lessons[index_two] = lessons[index_two], lessons[index_one]
            if ex1 in lessons:
                lessons.remove(ex1)
                lessons.insert(lessons.index(lesson) + 1, ex1)
            if ex2 in lessons:
                lessons.remove(ex2)
                lessons.insert(lessons.index(second_lesson) + 1, ex2)

    elif action == "Exercise":
            exercise = f"{lesson}-Exercise"
            if lesson in lessons:
                if exercise not in lessons:
                    idx = lessons.index(lesson)
                    lessons.insert(idx + 1, exercise)
            else:
                lessons.append(lesson)
                lessons.append(exercise)



    command = input()

index_lesson = 1
for lesson in lessons:
    print(f"{index_lesson}.{lesson}")
    index_lesson += 1