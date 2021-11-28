with open("text_1.txt", "w", encoding="utf-8") as task_1:
    for num_str in range(0, 1000):
        inp_str = input("add information: ")
        if len(inp_str) == 0:
            break
        else:
            task_1.write(f"{inp_str}\n")
