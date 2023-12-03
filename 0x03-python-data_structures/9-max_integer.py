#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_list = my_list.copy()
    max_list.sort()
    return max_list[-1]

