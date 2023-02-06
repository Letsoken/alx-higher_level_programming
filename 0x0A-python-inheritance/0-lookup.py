#!/usr/bin/python3
"""Task 0
"""


def lookup(obj):
    """Function returns list of attributes and methods of an object.

    Args:
        width: width of rectangle instance.
    Returns:
        The list of available attributes and methods of an object
    """

    return dir(obj)
