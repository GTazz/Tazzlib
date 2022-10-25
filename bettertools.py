from builtins import ValueError, IndexError
from os import get_terminal_size
from time import sleep


def erase_line(size):

    # Requer um único argumento.
    # O argumento define o tamanho numérico do output que, o mesmo, irá apagar.

    columns = int(str(get_terminal_size()).split('=')[1].split(',')[0])

    lines = 1
    while size >= columns:
        size -= columns
        lines += 1

    return [print(f'\33[A{" "*columns}\33[A') for c in range(0, lines)]


def name_input(the_input):
    while True:
        variable = input(the_input)
        size = len(the_input)+len(variable)
        variable = " ".join(variable.split()).title()
        if len(variable) == 0:
            erase_line(size)
            continue
        else:
            erase_line(size)
            print(f'{the_input}{variable}')
            break
    return variable


def int_input(the_input, error_message):

    # (1) O primeiro argumento define a string dentro do input.
    # (2) O segundo argumento define a mensagem de erro, em formato de string.

    message_size = len(error_message)
    while True:
        try:
            variable = input(the_input)
            size = len(the_input)+len(variable)
            variable = int(variable)
        except ValueError:
            erase_line(size)
            print(f'\33[91m{error_message}\33[m')
            sleep(1)
            erase_line(message_size)
            continue
        else:
            erase_line(size)
            print(f'{the_input}{variable}')
            break
    return variable


def opt_input(the_input,  options, error_message):

    # (1) O primeiro argumento define a string dentro do input.
    # (2) O segundo argumento define a mensagem de erro, em formato de string.
    # (3) O terceiro argumento define o critério para a validação,
    #  através de uma lista.

    message_size = len(error_message)
    while True:
        try:
            variable = input(the_input)
            size = len(the_input)+len(variable)
            variable = " ".join(variable.split()).upper()[0]
            if variable not in options and variable.lower() not in options:
                ''[0]
        except IndexError:
            erase_line(size)
            print(f'\33[91m{error_message}\33[m')
            sleep(1)
            erase_line(message_size)
            continue
        else:
            erase_line(size)
            print(f'{the_input}{variable}')
            break
    return variable
