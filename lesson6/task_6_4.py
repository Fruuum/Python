from random import choice


class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = int(speed)
        self.color = color
        self.name = name
        self.is_police = police

    def start(self):
        print(f"{self.name} starts trip")

    def stop(self):
        print(f"{self.name} finish trip")

    def direction(self):
        list_dir = ["south", "north", "east", "west"]
        print(f"{self.name} turn to the {choice(list_dir)}")

    def speedometr(self):
        print(f"Скорость {self.name} составила {self.speed} км/ч")


class Town_car(Car):
    def speedometr(self):
        print(f"{self.name} speed is {self.speed} км\ч. Вы превысили скорость!"
              if self.speed > 40 else super().speedometr())


class Sport_car(Car):
    pass


class Work_car(Car):
    def speedometr(self):
        print(f"{self.name} speed is {self.speed} км\ч. Вы превысили скорость!"
              if self.speed > 40 else super().speedometr())


class Police_car(Car):
    def __init__(self, speed, color, name, police=True):
        super().__init__(speed, color, name, police=True)


auto_pol = Police_car(129, "Green", "Ford")
auto_work = Work_car(66, "White", "GAZ")
auto_town = Town_car(55, "Dark Green", "Honda")
auto_sport = Sport_car(320, "Red", "Ferrari")

auto_pol.start()
auto_pol.direction()
auto_pol.speedometr()
auto_pol.stop()

auto_work.start()
auto_work.direction()
auto_work.speedometr()
auto_work.stop()

auto_town.start()
auto_town.direction()
auto_town.speedometr()
auto_town.stop()

auto_sport.start()
auto_sport.direction()
auto_sport.speedometr()
auto_sport.stop()
