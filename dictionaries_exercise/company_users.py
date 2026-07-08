company_and_employees_dictionary = {}

while True:
    command = input().split(" -> ")
    if len(command) == 1:
        break
    company_name, employee_id = command

    if company_name not in company_and_employees_dictionary.keys():
        company_and_employees_dictionary[company_name] = []
        company_and_employees_dictionary[company_name].append(employee_id)
    else:
        if employee_id not in company_and_employees_dictionary[company_name]:
            company_and_employees_dictionary[company_name].append(employee_id)


for company_name, employee_ids in company_and_employees_dictionary.items():
    print(company_name)
    for employee_id in employee_ids:
        print(f"-- {employee_id}")