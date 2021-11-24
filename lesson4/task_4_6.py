from itertools import count, cycle

new_list = []
for el in count(3):
    if el > 10:
        break
    else:
        new_list.append(el)
print(new_list)


step = 0
ltr_list = []
for ltr in cycle("WORLD"):
    if step > 19:
        break
    else:
        ltr_list.append(ltr)
        step += 1
print(ltr_list)
