schedule = {}
with open("text_6.txt", "r", encoding="utf-8") as task_6:
    for sch_str in task_6:
        sch_str = sch_str.replace("(пр)", "").replace("(л)", "").replace("(лаб)", "")\
                  .replace("-", "0").replace(":", "").split()
        schedule[sch_str[0]] = sum(map(int, sch_str[1:]))
    print(schedule)
