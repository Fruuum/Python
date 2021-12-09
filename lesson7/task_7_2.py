from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, tissue):
        self.tissue = tissue

    @property
    @abstractmethod
    def tiss_cons(self):
        pass

    def __add__(self, other):
        tissue_summary = self.tiss_cons + other.tiss_cons
        return f"общий расход ткани - {tissue_summary} метров"


class Coat(Clothes):
    @property
    def tiss_cons(self):
        return round(self.tissue / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def tiss_cons(self):
        return round(2 * self.tissue + 0.3)


coat = Coat(52)
suit = Suit(182)
print(coat + suit)
