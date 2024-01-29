#!/usr/bin/python3
def uppercase(str):
    for i in str:
        charupper = ord(i)
        if (96 <= ord(i) <= 123):
            charupper -= 32
        print("{:c}".format(charupper), end='')
    print()
