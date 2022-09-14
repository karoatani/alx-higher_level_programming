#!/usr/bin/python3
def _len(li):
    num = 0
    for i in li:
        num += 1
    return num


def safe_print_list(my_list=[], x=0):
    try:
        [print(my_list[index], end='') for index, i in enumerate(range(x))]
    except IndexError:
        return _len(my_list)
    finally:
        print()
    return x
