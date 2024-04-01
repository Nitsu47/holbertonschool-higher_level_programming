#!/usr/bin/python3
"""adds all arguments to a Python list, and then save them to a file"""
import sys
from sys import argv
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if exists("add_item.json"):
    data = load_from_json_file("add_item.json")
else:
    data = []

for i in range(1, len(argv)):
    data.append(argv[i])

save_to_json_file(data, "add_item.json")
