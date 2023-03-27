import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        self.current_rolled = 0

    def roll_dice(self):
        self.current_rolled = random.randint(1, self.sides)
        print("Dice roll: ", self.current_rolled)
        return self.current_rolled

class DoubleDice(Dice):
    def __init__(self, sides=6):
        super().__init__(sides)
        self.current_rolled1 = 0
        self.current_rolled2 = 0
        self.rolled_sum = 0

    def roll_double_dice(self):
        self.current_rolled1 = random.randint(1, self.sides)
        self.current_rolled2 = random.randint(1, self.sides)
        self.rolled_sum = self.current_rolled1 + self.current_rolled2

        print("Dices roll: ", self.current_rolled1, self.current_rolled2)
        return self.current_rolled1, self.current_rolled2, self.rolled_sum