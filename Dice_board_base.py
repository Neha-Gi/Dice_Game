from Dice import D8
import Dice
class DummyDice():
    def __init__(self):
       self.dice = [D8()]

    def roll(self) -> None:
        for dice in self.dice:
            dice.roll()

   

    def __add__(self, other:Dice) -> None:
        if isinstance(other, Dice):
            self.dice.append(other)

    @property
    def total(self) -> int:
        return sum(dice.total for dice in self.dice)        