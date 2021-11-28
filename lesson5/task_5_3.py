with open("text_3.txt", "r", encoding="utf-8") as task_3:
    staff_dict = {line.split()[0]: float(line.split()[1]) for line in task_3}
    aver_salary = sum(staff_dict.values()) / len(staff_dict)
    print(f"зарабатывают больше 20 тыс. {[el[0] for el in staff_dict.items() if el[1] > 20000]}")
    print(f"средняя зарплата сотрудников равна {round(aver_salary, 2)}")
