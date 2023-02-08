#!/usr/bin/python3
"""Defines an inherited class Mylist."""


class Mylist(list):
    """Implements sorted list printing for base class list"""

    def print_sorted(self):
        """Prints the list in ascending sort"""
        print(sorted(self))
