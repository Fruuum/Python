class ZeroDiv(Exception):
    def __init__(self, txt):
        self.txt = txt


n_1 = input("введите делимое: ")
n_2 = input("введите делитель: ")

try:
    n_1 = float(n_1)
    n_2 = float(n_2)
    if n_2 == 0:
        raise ZeroDiv("Деление на 0 недопустимо!")
except (ValueError, ZeroDiv) as err:
    print(err)
else:
    print(round((n_1 / n_2), 2))
