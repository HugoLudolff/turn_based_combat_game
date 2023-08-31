# Import random to simulate dice rolls #
import random
# import time to add a delay between the turns #
import time

# Create the main menu #
def menu():
    menu = """
========= MENU =========
[1] Start
[2] Quit
--> """
    return input(menu)

# Create the menu shown during battle #
def menu_batalha():
    menu_batalha = """
========= BATTLE ==========
[1] - Sword
[2] - Magic
[3] - Run
--> """
    return input(menu_batalha)

# Constants #
PLAYER_HEALTH = 1000
SWORD_DAMAGE = 20
MAGIC_DAMAGE = 45
PLAYER_ARMOR = 10
GOBLIN_MAX_HEALTH = 500  
GOBLIN_DAMAGE = 10
GOBLIN_DEFENSE = 25



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
    
# Function called when its the player turn #
def player_turn():
    dano = 0
    escaped = 0
    option = menu_batalha()

    if option == '1':
        dano = sword_attack(GOBLIN_DEFENSE)
    elif option == '2':
        dano = magic_attack(GOBLIN_DEFENSE)
    elif option == '3':
        print('You ran away!')
        escaped+=1
    
    return dano, escaped

# Function called when its the goblin turn #            
def goblin_turn():
    dano = 0
    
    dano = goblin_attack(PLAYER_ARMOR)
    return dano


# BATTLE FUNCTION! #
def battle():
    # variables used in this function #
    player_vida = PLAYER_HEALTH
    goblin_vida = GOBLIN_MAX_HEALTH
    escaped = 0
    dano_player = 0

    while True:
        dano_player, escaped = player_turn()
        goblin_vida-=dano_player
        # delay #
        time.sleep(1)
        player_vida = player_vida - goblin_turn()
        print(f'Your health is {player_vida}')
        print(f'Goblin health is {goblin_vida}')
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


# main function #
def main():
    option = menu()

    while option != 0:
        if option == '1':
            battle()
            break
        elif option == '2':
            break
        else:
            print('Invalid Input!')
            break
    

main()