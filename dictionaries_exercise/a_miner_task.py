resources_dictionery = {}

while True:
    current_resource = input()
    if current_resource == "stop":
        break
    quantity = int(input())

    if current_resource not in resources_dictionery:
        resources_dictionery[current_resource] = 0
        resources_dictionery[current_resource] += quantity

    else:
        resources_dictionery[current_resource] += quantity


for resource, quantity in resources_dictionery.items():
    print(f"{resource} -> {quantity}")