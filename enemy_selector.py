import random
from orc import orc_attack
from goblin import goblin_attack

def enemy_selector():
    enemy_selected = random.randint(1,2)
    inimigo = 0
    if enemy_selected == 1:
        inimigo+=1
    else:
        pass
    return inimigo

def enemy(player_armor):

    while True:
        inimigo = enemy_selector()
        dano = 0
        if inimigo == 1:
            dano = orc_attack(player_armor)
        else:
            dano = goblin_attack(player_armor)
        
        return dano