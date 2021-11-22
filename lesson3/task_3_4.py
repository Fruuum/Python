# вариант1
def my_func(x, y):
    if x > 0 and y < 0:
        rez1 = x ** y
        print(round(rez1, 8))
    else:
        print("error")
        return


my_func(float(input("значение x: ")), int(input("значение y: ")))
