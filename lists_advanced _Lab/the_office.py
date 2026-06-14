employees = input().split()
factor = int(input())
employees = list(map(lambda x: int(x) * factor, employees))
filtred_list = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))
if len(filtred_list) >= (len(employees) / 2):
    result = f"Score: {len(filtred_list)}/{len(employees)}. Employees are happy!"
else:
    result = f"Score: {len(filtred_list)}/{len(employees)}. Employees are not happy!"
print(result)
