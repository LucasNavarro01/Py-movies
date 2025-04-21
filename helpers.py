import os

from termcolor import cprint

def clear_console():
    if os.name == 'nt':
        os.system('cls') # Para Windows
    else:
        os.system('clear') # Para linux

def show_menu():
    cprint('--- My Movies ---', 'red', attrs=['bold', 'blink'])
    cprint('1. Ver lista de Películas', 'blue')
    cprint('2. Agregar Película', 'blue')
    cprint('3. Ver info de una Película', 'blue')
    cprint('4. Editar Película', 'blue')
    cprint('5. Eliminar Película', 'blue')
    print()
    cprint('0. Salir', 'red', attrs=['bold'])