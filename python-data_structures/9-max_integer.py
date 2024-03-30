#!/usr/bin/python3
def max_integer(my_list=[]):
    max = my_list[0]
    for is_max in my_list:
        if is_max > max:
            max = is_max
    return max
