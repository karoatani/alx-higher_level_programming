#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list:
        get_sum = sum(map(lambda x: x[0] * x[1], my_list))
        get_part = sum(map(lambda x: x[1], my_list))
        return (get_sum / get_part)
    return 0
