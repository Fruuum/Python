class Road:
    def __init__(self):
        self._length = 5000
        self._width = 20

    def calculate(self, height, mass_psq=25):
        print(f"Масса асфальта для покрытия дороги длиной {self._length} м, шириной {self._width} м "
              f"и толщиной {height} см составляет {self._length * self._width * mass_psq * height / 1000} тонн")


m1 = Road()
m1.calculate(int(input("введите толщину асфальтового полотна: ")))
