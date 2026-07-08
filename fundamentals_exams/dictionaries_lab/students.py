students_dict = {}

while True:
    
    students = input().split(":")
    if len(students) == 1:
        students_new = " ".join(students[0].split("_"))
        break
    name, id, course = students
    
    students_dict[id] = [name, course]

for id, [name, course] in students_dict.items():
    if course == students_new:
        print(f"{name} - {id}")



