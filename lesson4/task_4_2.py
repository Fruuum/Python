start_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

fin_list = [start_list[el] for el in range(1, len(start_list)) if start_list[el] > start_list[el - 1]]
print(fin_list)
