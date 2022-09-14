#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        [print(my_list[index], end='') for index, i in enumerate(range(x))]
    except IndexError:
        return len(my_list)
    finally:
        print()
    return x
