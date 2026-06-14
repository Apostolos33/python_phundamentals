number_of_rooms = int(input())
room = 0
result = ""
total_chairs = 0
total_visitors = 0

for room in range(number_of_rooms):
    room += 1
    information = input().split()
    chairs, visitors = len(information[0]), int(information[1])
    total_chairs += chairs
    total_visitors += visitors
    if chairs < visitors:
        result += f"{visitors - chairs} more chairs needed in room {room}\n"

if total_chairs >= total_visitors:
    print(f"Game On, {abs(total_visitors - total_chairs)} free chairs left")
else:
    print(result)
    


