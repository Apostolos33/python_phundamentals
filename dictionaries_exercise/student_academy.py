students_and_their_grades = {}

number_of_students = int(input())

for student in range(number_of_students):
    name = input()
    grade = float(input())

    if name not in students_and_their_grades.keys():
        students_and_their_grades[name] = [0]
        students_and_their_grades[name][0] += grade
        students_and_their_grades[name].append(1)
    else:
        students_and_their_grades[name][0] += grade
        students_and_their_grades[name][1] += 1


for student, value in students_and_their_grades.items():
    avg_grade = students_and_their_grades[student][0] / students_and_their_grades[student][1]
    if avg_grade >= 4.5:
        print(f"{student} -> {avg_grade:.2f}")