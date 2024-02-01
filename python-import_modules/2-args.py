#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    num_argv = len(argv)
    if num_argv == 1:
        print("{} arguments.".format(num_argv - 1))
    elif (num_argv == 2):
        print("{} argument:".format(num_argv - 1))
    else:
        print("{} arguments:".format(num_argv - 1))
    for argindex, arg in enumerate(argv[1:], start=1):
        print("{}: {}".format(argindex, arg))
