force_book = {}

command = input()
while command != "Lumpawaroo":
    
    if " | " in command:
        force_side, force_user = command.split(" | ")
        
        user_exists = False
        for side, users in force_book.items():
            if force_user in users:
                user_exists = True
                break

        if not user_exists:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif " -> " in command:
        force_user, force_side = command.split(" -> ")
        
        for side, users in force_book.items():
            if force_user in users:
                users.remove(force_user)
                break
        if force_side not in force_book:
            force_book[force_side] = []
        force_book[force_side].append(force_user)
        
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")