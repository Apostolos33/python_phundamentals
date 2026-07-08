students_and_courses = {}

while True:
    command = input().split(" : ")
    if len(command) == 1:
        break

    course_name, student_name = command

    if course_name in students_and_courses.keys():
        students_and_courses[course_name][0] += 1
        students_and_courses[course_name][1].append(student_name)
        
    else:
        students_and_courses[course_name] = [0]
        students_and_courses[course_name][0] += 1
        students_and_courses[course_name] += [[student_name]]

for course, value in students_and_courses.items():
    print(f"{course}: {value[0]}")
    for student in value[1]:
        print(f"-- {student}")

