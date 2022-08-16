import random

class WaterEnemy:
    name = "Wave Ninja"
    health = 25
    type = 'water'
    weakness = 'earth'

    def attack(self, player):
        best = [
            'landed attack',
            'landed attack',
            'landed attack',
            'landed a CRITICAL HIT!',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        mid = [
            'attack missed...',
            'landed attack',
            'landed attack',
            'landed attack',
            'attack missed...',
            'attack missed...',
        ]

        weak = [
            'attack missed...',
            'attack missed...',
            'attack missed...',
            'landed attack',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        # player str and enemy wk
        if type == player.weakness:
            result = best[random.randint(0, len(best) - 1)]
            return result

        # player str but not enemy wk
        elif type == player.element_type:
            result = weak[random.randint(0, len(weak) - 1)]
            return result

        else:
            result = mid[random.randint(0, len(mid) - 1)]
            return result

    def take_damage(self, result, player):
        hit = 0

        if result == "You landed your attack" and player.element_type == self.weakness:
            hit += 5
            return hit
        elif result == "You landed your attack" and player.element_type != self.weakness:
            hit += 3
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type == self.weakness:
            hit += 10
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type != self.weakness:
            hit += 6
            return hit

        elif result == "Your attack missed...":
            return hit

# fire enemy
class FireEnemy:
    name = "Flame Ninja"
    health = 25
    type = 'fire'
    weakness = 'water'

    def attack(self, player):
        best = [
            'landed attack',
            'landed attack',
            'landed attack',
            'landed a CRITICAL HIT!',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        mid = [
            'attack missed...',
            'landed attack',
            'landed attack',
            'landed attack',
            'attack missed...',
            'attack missed...',
        ]

        weak = [
            'attack missed...',
            'attack missed...',
            'attack missed...',
            'landed attack',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        # player str and enemy wk
        if type == player.weakness:
            result = best[random.randint(0, len(best) - 1)]
            return result

        # player str but not enemy wk
        elif type == player.element_type:
            result = weak[random.randint(0, len(weak) - 1)]
            return result

        else:
            result = mid[random.randint(0, len(mid) - 1)]
            return result

    def take_damage(self, result, player):
        hit = 0

        if result == "You landed your attack" and player.element_type == self.weakness:
            hit += 5
            return hit
        elif result == "You landed your attack" and player.element_type != self.weakness:
            hit += 3
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type == self.weakness:
            hit += 10
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type != self.weakness:
            hit += 6
            return hit

        elif result == "Your attack missed...":
            return hit

# earth enemy
class EarthEnemy:
    name = "Soil Ninja"
    health = 25
    type = 'earth'
    weakness = 'fire'

    def attack(self, player):
        best = [
            'landed attack',
            'landed attack',
            'landed attack',
            'landed a CRITICAL HIT!',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        mid = [
            'attack missed...',
            'landed attack',
            'landed attack',
            'landed attack',
            'attack missed...',
            'attack missed...',
        ]

        weak = [
            'attack missed...',
            'attack missed...',
            'attack missed...',
            'landed attack',
            'landed a CRITICAL HIT',
            'attack missed...',
        ]

        # player str and enemy wk
        if type == player.weakness:
            result = best[random.randint(0, len(best) - 1)]
            return result

        # player str but not enemy wk
        elif type == player.element_type:
            result = weak[random.randint(0, len(weak) - 1)]
            return result

        else:
            result = mid[random.randint(0, len(mid) - 1)]
            return result

    def take_damage(self, result, player):
        hit = 0

        if result == "You landed your attack" and player.element_type == self.weakness:
            hit += 5
            return hit
        elif result == "You landed your attack" and player.element_type != self.weakness:
            hit += 3
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type == self.weakness:
            hit += 10
            return hit

        elif result == "You landed a CRITICAL HIT!" and player.element_type != self.weakness:
            hit += 6
            return hit

        elif result == "Your attack missed...":
            return hit