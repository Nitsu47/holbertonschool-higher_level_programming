#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        index = 0
        for element in row:
            print("{:d}".format(element), end="" if len(row) - 1 == index else " ")
        print()
