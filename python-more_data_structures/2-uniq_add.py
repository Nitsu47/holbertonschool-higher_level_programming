#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for add_num in set(my_list):
        total += add_num
    return (total)
