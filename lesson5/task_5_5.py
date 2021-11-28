from random import randint
list_numb = [randint(0, 1000) for _ in range(0, randint(0, 20))]
with open("text_5.txt", "w+", encoding="utf-8") as task_5:
    task_5.write(" ".join(map(str, list_numb)))
    task_5.seek(0)
    print(f"значения списка чисел - {task_5.read()}")
    task_5.seek(0)
    print(f"сумма значений равна {sum(map(int, task_5.readline().split()))}")

