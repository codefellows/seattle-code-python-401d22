# Handle rolling dice
# Add roll_dice static method to GameLogic class.
# The input to roll_dice is an integer between 1 and 6.
# The output of roll_dice is a tuple with random values between 1 and 6.
# The length of tuple must match the argument given to roll_dice method.
import random


class GameLogic:
    pass

    @staticmethod
    def roll_dice(num_dice):
        # return tuple(random.randint(1, 6) for _ in range(num_dice))
        dice_values = []
        for _ in range(num_dice):
            value = random.randint(1, 6)
            dice_values.append(value)
        return tuple(dice_values)

    @staticmethod
    def calculate_score(dice):
        if dice == (5,):
            return 50


class Banker:
    """Banker is reponsible for tracking points "on the shelf" and "in the bank"
    version_1
    """
    def __init__(self):
        self.balance = 0  # 200
        self.shelved = 0  # 0

    def bank(self):
        amount_deposited = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_deposited

    def shelf(self, amt):
        self.shelved += amt

    def clear_shelf(self):
        self.shelved = 0
