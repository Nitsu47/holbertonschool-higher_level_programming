#!/usr/bin/python3
"""Creates 'MyList' class thath inherits from list"""


class MyList(list):
    """defines the class MyList"""
    def print_sorted(self):
        """prints a sorted list in asc order"""
        new_list = self.copy()
        new_list.sort()
        print(new_list)
