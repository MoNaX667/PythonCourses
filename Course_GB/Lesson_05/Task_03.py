# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их
# окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

user_data_file_path = "Task_03_Data.txt"

sum_salary = 0
employees_number = 0

with open(user_data_file_path) as employees:
    for employee in employees:
        employee_salary = None
        data = employee.replace("\n","").split(" ")

        # Parse employee_salary
        try:
            employee_salary = float(data[1])
        except ValueError:
            print(f"There is a incorrect value format: {data[1]}. Skip this employee. Please check data")
            continue

        if (employee_salary != None) and (employee_salary < 20000):
            print(f"{data[0]} has salary lower than 20000 rubles ({employee_salary})")

        # Increment system data
        sum_salary += employee_salary
        employees_number += 1

middle_salary = sum_salary / employees_number

print(f"Middle salary for the {employees_number} employees is {middle_salary}")

