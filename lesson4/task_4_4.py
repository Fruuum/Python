rand_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
un_list = [el for el in rand_list if rand_list.count(el) == 1]
print(un_list)