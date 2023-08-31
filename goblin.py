import random


GOBLIN_MAX_HEALTH = 500  
GOBLIN_DAMAGE = 10
GOBLIN_DEFENSE = 25
# Function called when the goblin attacks #
def goblin_attack(player_defense):
    dado_dano = random.randint(1, 20)
    dado_defesa = random.randint(1, 20)
    dano = (dado_dano * GOBLIN_DAMAGE) - (dado_defesa * player_defense)
    if dano <= 0:
        dano = 0
        print("Goblin missed!")
    else:
        print(f'Goblin did {dano} damage!\n')
    return dano


def goblin_turn(player_armor):
    dano = 0
    
    dano = goblin_attack(player_armor)
    return dano

