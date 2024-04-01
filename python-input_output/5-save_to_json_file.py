#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file using JSON"""
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
