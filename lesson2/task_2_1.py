my_str = 'just do it'
my_tuple = (1, 23.3, 'qwa', ['q', 'a', 'z'],)
my_dict = {1: 1, 32: 2, 449: 3}
my_list = ['a', 'b', 'c', 'd', 'e']
new_list = [12, 2.3, 23 + 1j, True, "AaA", my_dict, my_str, my_tuple, my_list, my_str]
for el in new_list:
    print(type(el))
