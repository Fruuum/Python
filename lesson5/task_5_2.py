task_2 = open("text_4.txt", "r", encoding="utf-8")
i = 0
for n in task_2:
    i += 1
task_2.seek(0)
for m in range(i):
    len_str = len(list(task_2.readline().split()))
    print(f"в {m + 1}-й строке {len_str} элементов")
print(f"в файле {i} строк")
task_2.close()
