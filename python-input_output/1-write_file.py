#!/usr/bin/python3
""" Writes to a file and returns the number of characters"""


def write_file(filename="", text=""):
    """Open a given file and writes on it"""
    with open(filename, "w", encoding="utf-8") as file:
        nums = file.write(text)
    return nums
