#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for y in set(my_list):
        sum += y
    return sum
