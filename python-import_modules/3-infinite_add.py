#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    result = 0
    arg_count = 0
    for args in argv:
        if arg_count != 0:
            result = result + int(args)
        arg_count += 1
    print("{}".format(result))
