some_data = input("введите значения: ").split()
print("начальный вариант", some_data)
n = len(some_data) % 2
if n != 0:
    data1 = some_data[:-1]
    data1[::2], data1[1::2] = data1[1::2], data1[::2]
    print("измененный вариант", data1 + [some_data[-1]])
else:
    some_data[::2], some_data[1::2] = some_data[1::2], some_data[::2]
    print('измененный вариант', some_data)
