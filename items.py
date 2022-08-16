import random


class Weapon:
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return str(self.type)

    def attack(self):
        result = ""
        action = [
            'You landed your attack',
            'You landed a CRITICAL HIT!',
            'You landed your attack',
            'You landed a CRITICAL HIT!',
            'Your attack missed...',
            'Your attack missed...']

        result = action[random.randint(0, len(action) - 1)]
        return result


class HealthItem:

    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return str(self.type)

    def consume(self):
        health_regain = 2
        energy_regain = 4

        return health_regain, energy_regain
