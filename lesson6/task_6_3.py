class Worker:
    def __init__(self, name, surname, position, wage_val, bonus_val):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage_val, "bonus": bonus_val}


class Position(Worker):
    def get_full_name(self):
        print(f"На должность <{self.position}> назначен {self.name} {self.surname}")

    def get_total_income(self):
        print(f"Общий доход {self.name} составляет {sum(self._income.values())} р.")


worker_1 = Position("Иоанн Васильевич", "Грозный", "Царь", 100000, 25000)
worker_1.get_full_name()
worker_1.get_total_income()
