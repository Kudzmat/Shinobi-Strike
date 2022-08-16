import random
from items import Weapon, HealthItem
from Shinobi import Shinobi
from Enemy import WaterEnemy, EarthEnemy, FireEnemy


# elements - fire, water, earth
# fight_style - close combat, weapons, ranged

# classes - health item, throwing weapon, enemy1, enemy2,

# SWORD_ATTACKS[random.randint(0, len(SWORD_ATTACKS) - 1)]
# SWORD_ATTACKS = ['Your attack missed...',
#                  'You landed your attack',
#                  'You both landed a hit',
#                  'You both landed a hit',
#                  'You both landed a hit',
#                  'Your attack missed...',
#                  ]

def loss():
    return "you have been defeated! You Lose!"


def victory(player):
    return f"***** You Win! {player.name}, you are the the strongest SHINOBI!! ******"


# when a player selects to use a justsu
def justu_attack(player, enemy, energy):
    if energy > 0:
        print("Select a justsu type: ")
        option = int(input("(1). Fire justu   (2). Water justu   (3). Earth justu     (4). Back"))

        # fire
        if option == 1:
            player_result, energy_consumed = player.fire_justu()
            print(player_result)
            player_hit = enemy.take_damage(player_result, player)  # the damage result of justu attack
            print(f"{enemy.name} took {player_hit} damage.")
            print()

            enemy_result = enemy.attack(player)
            print(f"{enemy.name} lunges toward you")
            print(enemy_result)
            enemy_hit = player.take_damage(enemy_result, enemy)
            print(f"You took {enemy_hit} damage")

            return enemy_hit, player_hit, energy_consumed

        # water
        elif option == 2:
            player_result, energy_consumed = player.water_justu()
            print(player_result)
            player_hit = enemy.take_damage(player_result, player)  # the damage result of justu attack
            print(f"{enemy.name} took {player_hit} damage.")
            print()

            enemy_result = enemy.attack(player)
            print(f"{enemy.name} lunges toward you")
            print(enemy_result)
            enemy_hit = player.take_damage(enemy_result, enemy)
            print(f"You took {enemy_hit} damage")

            return enemy_hit, player_hit, energy_consumed

        # earth
        elif option == 3:
            player_result, energy_consumed = player.earth_justu()
            print(player_result)
            player_hit = enemy.take_damage(player_result, player)  # the damage result of justu attack
            print(f"{enemy.name} took {player_hit} damage.")
            print()

            enemy_result = enemy.attack(player)
            print(f"{enemy.name} lunges toward you")
            print(enemy_result)
            enemy_hit = player.take_damage(enemy_result, enemy)
            print(f"You took {enemy_hit} damage")

            return enemy_hit, player_hit, energy_consumed


    # player is punished for trying to use justu with no energy left
    else:
        print("You stumbled and fell because you have no energy left")
        enemy_result = enemy.attack(player)
        print(f"{enemy.name} lunges toward you")
        print(enemy_result)
        enemy_hit = player.take_damage(enemy_result, enemy)
        print(f"You took {enemy_hit} damage")

        return 0, enemy_hit, 0


# when the player elects to use an item
def use_item(tools):
    if tools:  # checks to see if the player has any items in tools
        pockets = {}

        for num, tool in enumerate(tools):
            pockets[num + 1] = tool

        for num, item in pockets.items():
            print(f"({num}). {item}")

        option = int(input("select an item to use:"))

        item_name = pockets[option]
        item_index = option - 1  # item's index
        choice = tools[item_index]
        health_regain, energy_regain = choice.consume()
        print(f"You used {item_name}, it restored {energy_regain} energy and {health_regain} health!")
        tools.pop(item_index)  # removing the item from pockets

        return tools, health_regain, energy_regain

    else:
        print("You have no more items in your pockets")  # no more items left


def use_weapon(weapons, enemy, player):
    if weapons:
        pockets = {}  # empty dictionary will store weapons and link it with a key for selection purposes

        for num, weapon in enumerate(weapons):  # enumerate() will assign a number to each weapon
            pockets[num + 1] = weapon  # storing into dictionary

        for num, item in pockets.items():
            print(f"({num}). {item}")  # showing player weapons with corresponding number

        option = int(input("select an item to use:"))

        item_name = pockets[option]  # getting weapon's name in dictionary using key
        item_index = option - 1  # weapon's index in list is the number it appears on screen - 1
        choice = weapons[item_index]  # getting the actual weapon selected via its index in list
        print(f" You attacked with your {item_name}")
        weapon_result = choice.attack()  # did the weapon attack succeed
        print(weapon_result)
        weapon_damage = enemy.take_damage(weapon_result, player)
        print(f"{enemy.name} took {weapon_damage} damage.")
        weapons.pop(item_index)  # removing the weapon from pockets

        # enemy turn
        enemy_result = enemy.attack(player)
        print(f"{enemy.name} lunges toward you")
        print(enemy_result)
        enemy_hit = player.take_damage(enemy_result, enemy)
        print(f"You took {enemy_hit} damage")

        return weapons, weapon_damage, enemy_hit


def battle(player, enemy, tools, weapons):
    game_on = True  # keeps the game going
    player_health = player.health  # players health
    player_energy = player.energy
    enemy_health = enemy.health  # enemy's health
    winner = 0  # returns 1 if the player wins, or 2 if the enemy wins

    print()

    while game_on:
        if player_health <= 0:
            winner += 2
            return winner

        elif enemy_health <= 0:
            winner += 1
            return winner

        else:

            print(f"""
                    {enemy.name} * ----- * HP: {enemy_health}
                    ----------------------------------------
                    ----------------------------------------
                    {player.name} *** ----- *** HP: {player_health}   Energy: {player_energy}/10
                """)
            print("What action will you take:")
            option = int(input("(1). Attack     (2). Items     (3). Ninja Weapons"))

            if option == 1:
                print()
                """
                attack option returns player damage, enemy damage and energy used after attack
                """
                player_damage, enemy_damage, energy_used = justu_attack(player, enemy, player_energy)
                player_health -= player_damage
                enemy_health -= enemy_damage
                player_energy -= energy_used

            # using items
            elif option == 2:
                print()
                if tools:
                    tools, health_regain, energy_regain = use_item(tools)
                    player_energy += energy_regain
                    player_health += health_regain
                else:
                    print("You have no more items left")

            # using ninja weapon
            elif option == 3:
                print()
                if weapons:
                    weapons, enemy_damage, player_damage = use_weapon(weapons, enemy, player)
                    enemy_health -= enemy_damage
                    player_health -= player_damage

                else:
                    print("You have no more weapons left")


menu = True

while menu:
    print("Welcome to Shinobi battle, please enter your name. ")

    # player details
    name = input("Enter name: ")
    print("Please select an element type.")
    element_type = int(input("(1). fire     (2). water     (3). earth"))
    if element_type == 1:
        element_type = 'fire'

    elif element_type == 2:
        element_type = 'water'

    elif element_type == 3:
        element_type = 'earth'

    # create player
    ninja1 = Shinobi(name, element_type)

    # creating an enemy using random
    enemy_types = ['water', 'earth', 'fire']
    opponent = enemy_types[random.randint(0, len(enemy_types) - 1)]
    if opponent == 'water':
        grunt = WaterEnemy()

    elif opponent == 'earth':
        grunt = EarthEnemy()

    else:
        grunt = FireEnemy()

    # create weapons and health items for player
    weapon1 = Weapon("kunai")
    weapon2 = Weapon("shiruken")
    weapon3 = Weapon("Giant shiruken")

    health1 = HealthItem('shushi')
    health2 = HealthItem('burger')
    health3 = HealthItem('energy drink')

    tools = [health1, health2, health3]
    swords = [weapon1, weapon2, weapon3]

    print()
    print("----------------------------------")
    result = battle(ninja1, grunt, tools, swords)

    if result == 2:
        game_over = loss()
        print("----------------------------------")
        print(game_over)

    else:
        game_complete = victory(ninja1)
        print("----------------------------------")
        print(game_complete)
