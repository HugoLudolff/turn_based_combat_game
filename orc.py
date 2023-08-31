import random


ORC_MAX_HEALTH = 1000  
ORC_DAMAGE = 20
ORC_DEFENSE = 70
# Function called when the orc attacks #
def orc_attack(player_defense):
    dado_dano = random.randint(1, 20)
    dado_defesa = random.randint(1, 20)
    dano = (dado_dano * ORC_DAMAGE) - (dado_defesa * player_defense)
    if dano <= 0:
        dano = 0
        print("Orc missed!")
    else:
        print(f'Orc did {dano} damage!\n')
    return dano


def orc_turn(player_armor):
    dano = 0
    
    dano = orc_attack(player_armor)
    return dano
