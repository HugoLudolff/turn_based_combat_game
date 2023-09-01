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


def menu_inimigo():
    menu_inimigo = """
====== ENEMY =======
Pick an enemy to fight!

[1] - Goblin
[2] - Orc
[3] - Quit
--> """
    return input(menu_inimigo)