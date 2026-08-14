followers = {}

command = input()

while command != "Log out":
    command_as_list = command.split(": ")
    action = command_as_list[0]
    username = command_as_list[1]
    if action == "New follower":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 0}

    elif action == "Like":
        count = int(command_as_list[2])
        if username not in followers:
            followers[username] = {"likes": count, "comments": 0}
        else:
            followers[username]["likes"] += count

    elif action == "Comment":
        if username not in followers:
            followers[username] = {"likes": 0, "comments": 1}
        else:
            followers[username]["comments"] += 1

    elif action == "Blocked":
        if username in followers:
            del followers[username]
        else:
            print(f"{username} doesn't exist.")




    command = input()

print(f"{len(followers)} followers")

for key, value in followers.items():
    username = key
    likes_and_comments = value["likes"] + value["comments"]
    print(f"{username}: {likes_and_comments}")