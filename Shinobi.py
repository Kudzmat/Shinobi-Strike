import random


class Shinobi:
    health = 20
    energy = 10

    def __init__(self, name, element_type, special_move=None, weakness=None):
        self.name = name
        self.element_type = element_type

        if element_type == "fire":
            self.special_move = "Grand Solar Fireball"
            self.weakness = 'water'

        elif element_type == "water":
            self.special_move = "Atlantic Tidal Wave"
            self.weakness = 'earth'

        elif element_type == "earth":
            self.special_move = "Earthquake Crusher"
            self.weakness = 'fire'

    def take_damage(self, enemy_damage_result, enemy):
        hit = 0

        if enemy_damage_result == "landed attack" and self.weakness == enemy.type:
            hit += 5
            return hit
        elif enemy_damage_result == "landed attack" and self.weakness != enemy.type:
            hit += 3
            return hit

        if enemy_damage_result == "landed a CRITICAL HIT!" and self.weakness == enemy.type:
            hit += 10
            return hit
        elif enemy_damage_result == "landed a CRITICAL HIT!" and self.weakness != enemy.type:
            hit += 6
            return hit

        if enemy_damage_result == "attack missed...":
            return hit

    def fire_justu(self):  # takes the enemy object as a parameter
        attack_result = ""  # if the attack landed or not
        energy_consumed = 0  # if it's a special attack, energy will be consumed

        if self.element_type == 'fire':
            best = [
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'You landed a CRITICAL HIT!',
                'You landed a CRITICAL HIT!',
                'Your attack missed...',
            ]
            attack_result = best[random.randint(0, len(best) - 1)]
            print(f"You used {self.special_move} justu!")
            energy_consumed += 2
            return attack_result, energy_consumed

        elif self.weakness == 'fire':
            weak = [
                'Your attack missed...',
                'Your attack missed...',
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...',
            ]
            attack_result = weak[random.randint(0, len(weak) - 1)]
            print("You used fire spit justu.")
            energy_consumed += 3
            return attack_result, energy_consumed


        else:
            mid = [
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...',
                'Your attack missed...',
            ]
            attack_result = mid[random.randint(0, len(mid) - 1)]
            print("You used fire spit justu.")
            energy_consumed += 2
            return attack_result, energy_consumed

    # water justu
    def water_justu(self):
        attack_result = ""
        energy_consumed = 0

        if self.element_type == 'water':
            best = [
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'You landed a CRITICAL HIT!',
                'You landed a CRITICAL HIT!',
                'Your attack missed...',
            ]
            attack_result = best[random.randint(0, len(best) - 1)]
            print(f"You used {self.special_move} justu!")
            energy_consumed += 2
            return attack_result, energy_consumed

        elif self.weakness == 'water':
            weak = [
                'Your attack missed...',
                'Your attack missed...',
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...',
            ]
            attack_result = weak[random.randint(0, len(weak) - 1)]
            print("You used water spit justu.")
            energy_consumed += 3
            return attack_result, energy_consumed

        else:
            mid = [
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...',
                'Your attack missed...']
            attack_result = mid[random.randint(0, len(mid) - 1)]
            print("You used water spit justu.")
            energy_consumed += 2
            return attack_result, energy_consumed

    # earth justu
    def earth_justu(self):
        attack_result = ""
        energy_consumed = 0

        if self.element_type == 'earth':
            best = [
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'You landed a CRITICAL HIT!',
                'You landed a CRITICAL HIT!',
                'Your attack missed...']
            attack_result = best[random.randint(0, len(best) - 1)]
            print(f"You used {self.special_move} justu!")
            energy_consumed += 2
            return attack_result, energy_consumed

        elif self.weakness == 'earth':
            weak = [
                'Your attack missed...',
                'Your attack missed...',
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...']
            attack_result = weak[random.randint(0, len(weak) - 1)]
            print("You used mud slide justu.")
            energy_consumed += 3
            return attack_result, energy_consumed

        else:
            mid = [
                'Your attack missed...',
                'You landed your attack',
                'You landed your attack',
                'You landed your attack',
                'Your attack missed...',
                'Your attack missed...']
            attack_result = mid[random.randint(0, len(mid) - 1)]
            print("You used mud slide justu.")
            energy_consumed += 2
            return attack_result, energy_consumed
