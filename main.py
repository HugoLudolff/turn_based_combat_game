# Import random to simulate dice rolls #
import random
# import time to add a delay between the turns #
import time

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