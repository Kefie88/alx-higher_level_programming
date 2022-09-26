#!/usr/bin/python3
"""My List"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list, but sorted (ascending)"""
        print(sorted(self))
