#!/usr/bin/python3
"""Task 1
"""


class Mylist(list):
    """A subclass of the list class"""

    def print_sorted(self):
        """Function that prints the list, but sorted (ascending sort)"""
        print(sorted(self))
