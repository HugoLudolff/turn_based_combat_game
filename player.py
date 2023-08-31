import random
from menus import menu_batalha


# Constants #
PLAYER_HEALTH = 1000
SWORD_DAMAGE = 20
MAGIC_DAMAGE = 45
PLAYER_ARMOR = 50

# Function called when the player selects to attack with a sword #
def sword_attack(enemy_defense):
    # Rolls player attack dice #
    dado_dano = random.randint(1, 20)
    # Rolls enemy defense dice #
    dado_defesa = random.randint(1, 20)
    # Calculates how much damage the player did #
    dano = (dado_dano * SWORD_DAMAGE) - (dado_defesa * enemy_defense)
    # if the damage is less than 0, it turns to zero #
    # otherwise the enemy would gain health #
    if dano <= 0:
        dano = 0
        print("Miss!")
    else:
        pass
    print(f'Sword did {dano} damage!\n')
    return dano

# Function called when the player selects to attack with magic #
def magic_attack(enemy_defense):
    dado_dano = random.randint(1, 20)
    dado_defesa = random.randint(1, 20)
    # The enemy receives a +10 to its defense #
    # because magic does more damage but its less effective against armor #
    dano = dado_dano * MAGIC_DAMAGE - dado_defesa * (enemy_defense + 10)
    if dano <= 0:
        dano = 0
        print("Miss!")
    else:
        print(f'Magic did {dano} damage!\n')
    return dano

    
# Function called when its the player turn #
def player_turn(enemy_defense):
    dano = 0
    escaped = 0
    option = menu_batalha()

    if option == '1':
        dano = sword_attack(enemy_defense)
    elif option == '2':
        dano = magic_attack(enemy_defense)
    elif option == '3':
        print('You ran away!')
        escaped+=1
    
    return dano, escaped