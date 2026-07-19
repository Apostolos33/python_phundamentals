import re

command = input()

pattern = r"(w{3}\.[a-zA-Z0-9\-]+(\.[a-z]+)+)"

while command:

    matches = re.search(pattern, command)
    if matches:
        link = matches.group(1)
        print(link)

    command = input()