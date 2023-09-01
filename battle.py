import time
from player import *
from goblin import *
from orc import *
from menus import menu_inimigo

# Variables #
player_hitpoints = PLAYER_HEALTH
escaped = 0
dano_player = 0


def battle_goblin():
    goblin_vida = GOBLIN_MAX_HEALTH
    goblin_armor = GOBLIN_DEFENSE
    player_vida = PLAYER_HEALTH

    while True:
        # The Player turn is first #
        # It checks if the player escaped and if not the damage it did #
        dano_player, escaped = player_turn(goblin_armor)
        # The damage is then subtracted from the enemy hit points #
        goblin_vida-=dano_player
        # A small delay so it doesnt get confusing #
        time.sleep(1)
        # The enemys turn #
        # As only the damage its returned from the enemys turn function #
        # It gets directly subtracted from the players hp #
        player_vida = player_vida - goblin_turn(PLAYER_ARMOR)
        # Another small delay #
        time.sleep(1)
        # This prints the players hp after the turn #
        print(f'Your health is {player_vida}')
        # This prints the enemys hp after the turn #
        print(f'Goblin health is {goblin_vida}')
        # Third delay #
        time.sleep(1)
        # If the player decided to run, goes back to the main menu #
        if escaped == 1:
            break
        # Checks if the player and the goblin still have hp #
        elif player_vida > 0 and goblin_vida > 0:
            pass    
        # if the player is out of hp, prints that he died and goes back to the enemy selection menu #
        elif player_vida < 0:
            print('You died!')
            break
        # if the goblin died, prints that he was defeated and goes back to the enemy selction menu #
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
        time.sleep(1)
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
        if option == '2':
            battle_orc()
            break
        elif option == '1':
            battle_goblin()
            break
        elif option =='3':
            break
        else:
            print('Invalid input!')
            break
            
        