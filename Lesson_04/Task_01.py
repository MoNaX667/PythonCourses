# Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
import sys


def calculate_salary(prize=0, hourly_rate=10, covered_hours=0):
    """
    Functions calculates salary by the following formula (covered_hours * hourly_rate) + prize
    :param prize: prize
    :param hourly_rate: money per work hour
    :param covered_hours: completed hours
    :return:
    """
    salary = (covered_hours * hourly_rate) + prize

    return salary


# Parsing configuration arguments
file, worker_hours, worker_rate, worker_prize = sys.argv

print(f"The worker completed {worker_hours} hours")
print(f"The hourly rate is {worker_rate}")
print(f"The prize is {worker_prize}")

worker_salary = calculate_salary(covered_hours=int(worker_hours),
                                 hourly_rate=int(worker_rate),
                                 prize=int(worker_prize))

print(f"The worker will get {worker_salary} gross")
