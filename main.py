from menus import menu
from goblin import *
from orc import *
from player import *
from battle import battle


# main function #
def main():
    option = menu()

    while True:
        if option == '1':
            battle()
            break
        elif option == '2':
            break
        else:
            print('Invalid Input!')
            break
    

main()