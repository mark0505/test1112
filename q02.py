employee_list = []

while True:
    print("-" * 28)
    print("        員工薪資輸入        ")
    print("    若姓名處未輸入則代表結束")
    print("-" * 28)

    e_name = input("請輸入姓名:")

    if not e_name:
        break

    e_salary = float(input("請輸入薪資:"))

    employee = {"eName": e_name, "eSalary": e_salary}
    employee_list.append(employee)

print("-" * 28)
print("員工薪資清單")
print("-" * 28)

total_salary = 0

for emp in employee_list:
    total_salary += emp["eSalary"]
    print(f"員工{emp['eName']} 的薪資為 {emp['eSalary']:,.0f}")

average_salary = total_salary / len(employee_list)

print("-" * 28)
print(f"合計薪資：{total_salary: >15,.0f}")
print(f"平均薪資：{average_salary: >15,.2f}")
print("=" * 28)