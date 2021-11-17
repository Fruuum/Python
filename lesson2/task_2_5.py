rating_list = [7, 4, 2, 2, 1, 0]
new_value = int((input("введите новое целочисленное значение: ")))
ind = 0
for el in rating_list:
    if new_value <= el:
        ind += 1
    else:
        break
rating_list.insert(ind, new_value)
print(rating_list)

# решение через .append & .sort, насколько я понял, тоже добавляет новый элемент справа от тех,
# которые уже были в списке, но при этом программа, как мне кажется, менее ресурсоемкая. Я прав, или в этом решении
# есть скрытая ошибка?
rating_list = [7, 4, 2, 2, 1, 0]
new_value = int((input("введите новое целочисленное значение: ")))
rating_list.append(new_value)
rating_list.sort(reverse=True)
print(rating_list)
