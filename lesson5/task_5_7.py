from json import dump

with open('text_7.txt', "r", encoding="utf-8") as start_text:
    with open('text_77.json', "w", encoding="utf-8") as end_text:
        debt = {line.split()[0]: int(line.split()[2]) - int(line.split()[3]) for line in start_text}
        av_debt = []
        for el in debt.values():
            if el > 0:
                av_debt.append(el)
        dump([debt, {"средняя выручка": sum(av_debt) / len(av_debt)}], end_text, ensure_ascii=False)
