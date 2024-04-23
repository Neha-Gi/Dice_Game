from abc import ABC, abstractmethod
from random import randint

class Dice(ABC):
    def __init__(self):
        self.face = 0

    @abstractmethod
    def roll(self) -> None:
        pass

    @property
    def total(self) -> int:
        return self.face

class D8(Dice):
    def roll(self) -> None:
        self.face = randint(1, 8)

