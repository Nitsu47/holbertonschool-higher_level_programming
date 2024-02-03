#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num_el = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end='')
            num_el += 1
        except Exception:
            break
    print()
    return(num_el)
