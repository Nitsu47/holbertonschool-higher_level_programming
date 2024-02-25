#!/usr/bin/python3
"""Module read_file, reads the content of a file and prints it"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
