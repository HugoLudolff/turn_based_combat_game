from menus import menu
from battle import battle


# main function #
def main_menu():
    option = menu()
    quit = 0

    while True:
        if option == '1':
            battle()
            break
        elif option == '2':
            quit+=1
            break
        else:
            print('Invalid Input!')
            break
    return quit
    
while True:
    quit = 0
    quit+=main_menu()
    if quit == 0:
        main_menu()
    elif quit == 1:
        break