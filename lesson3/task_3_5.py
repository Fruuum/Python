def func_sum():
    total = 0
    while True:
        my_list = input("введите числа или 'Q' для выхода: ").split()
        for n in my_list:
            if n == "Q":
                return total
            else:
                try:
                    total += int(n)
                except ValueError as error:
                    print(error)
        print(total)


print(func_sum())
