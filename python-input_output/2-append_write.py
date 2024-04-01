#!/usr/bin/python3
"""Appends to a file"""


def append_write(filename="", text=""):
    """Open a given file and append on it"""
    with open(filename, "a", encoding="utf-8") as file:
        nums = file.write(text)
    return nums
