import time
from player import *
from goblin import *
from orc import *
from enemy_selector import *
from menus import menu_inimigo


player_hitpoints = PLAYER_HEALTH
escaped = 0
dano_player = 0


def battle_goblin():
    goblin_vida = GOBLIN_MAX_HEALTH
    goblin_armor = GOBLIN_DEFENSE
    player_vida = PLAYER_HEALTH

    while True:
        dano_player, escaped = player_turn(goblin_armor)
        goblin_vida-=dano_player
        time.sleep(1)
        player_vida = player_vida - goblin_turn(PLAYER_ARMOR)
        print(f'Your health is {player_vida}')
        print(f'Goblin health is {goblin_vida}')
        time.sleep(1)
        if escaped == 1:
            break
        elif player_vida > 0 and goblin_vida > 0:
            pass    
        elif player_vida < 0:
            print('You died!')
            break
        elif goblin_vida < 0:
            print('Goblin defeated!')
            break


def battle_orc():
    orc_vida = ORC_MAX_HEALTH
    orc_armor = ORC_DEFENSE
    player_vida = PLAYER_HEALTH

    while True:
        dano_player, escaped = player_turn(orc_armor)
        orc_vida-=dano_player
        time.sleep(1)
        player_vida = player_vida - orc_turn(PLAYER_ARMOR)
        print(f'Your health is {player_vida}')
        print(f'Orc health is {orc_vida}')
        time.sleep(1)
        if escaped == 1:
            break
        elif player_vida > 0 and orc_vida > 0:
            pass    
        elif player_vida < 0:
            print('You died!')
            break
        elif orc_vida < 0:
            print('Orc defeated!')
            break

def battle():
    option = menu_inimigo()
    while True:
        if option == '1':
            battle_orc()
            break
        elif option == '2':
            battle_goblin()
            break
        else:
            print('Invalid input!')
            break
        