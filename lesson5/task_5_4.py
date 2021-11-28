from translate import Translator
translator = Translator(from_lang="en", to_lang="ru")
out_file = open("task_4-1", "w", encoding="utf-8")
with open("text_4.txt", "r", encoding="utf-8") as task_4:
    i = 0
    for n in task_4:
        i += 1
    task_4.seek(0)
    for lines in range(i):
        out_file.write(f"{translator.translate(task_4.readline())}\n")
out_file.close()



        # new_obj.append(t_lines)  # print(new_obj)
        # "".join(new_str)

        # ("text_4-1.txt", "w", encoding="utf-8")
        # new_obj.write()
        # new_obj.close()


# print(trans_line)
