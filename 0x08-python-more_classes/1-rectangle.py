#!/usr/bin/python3
"""Defines an empty class called Rectangle that defines a rectangle"""


class Rectangle:
    """Defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes a rectangle instance

        Args:
            width: width of rectangle instance.
            height: height of rectangle instance.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieves width of rectangle instance."""

        return self.__width

    @width.setter
    def width(self, width):
        """Sets width of rectangle instance.

        Args:
            width: value of the width must be a positive integer
        """
        if not isinstance(width, int):
            raise typeerror("width must be an integer")
        if width < 0:
            raise valueerror("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """Retrieves height of rectangle instance."""

        return self.__height

    @height.setter
    def height(self, height):
        """Sets height of rectangle instance.

        Args:
            height: value of the height must be a positive integer
        """
        if not isinstance(height, int):
            raise typeerror("height must be an integer")
        if height < 0:
            raise valueerror("height must be >= 0")
        self.__height = height
