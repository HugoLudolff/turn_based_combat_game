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
======INIMIGO=======
escolha um inimigo para lutar!

[1] - Orc
[2] - Goblin
--> """
    return input(menu_inimigo)