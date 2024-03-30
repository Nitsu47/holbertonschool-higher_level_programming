#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    a = (0 if len(list_a) < 1 else list_a[0]) + (0 if len(list_b) < 1 else list_b[0])
    b = (0 if len(list_a) < 2 else list_a[1]) + (0 if len(list_b) < 2 else list_b[1])
    return (a, b)
