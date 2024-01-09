#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    big = my_list[0]
    for y in range(len(my_list)):
        if my_list[y] > big:
            big = my_list[y]
    return (big)
