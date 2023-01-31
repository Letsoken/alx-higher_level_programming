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
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
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
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """Calculate area of rectangle

        Return:
            The area of rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """Calculates perimeter of rectangle

        Returns:
            The rectangle perimeter
        """

        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns an “informal” and nicely printable
        string representation of a rectangle instance filled
        with the # character
        """

        if self.__width == 0 or self.__height == 0:
            return ''
        rect_ = ''
        for rows in range(self.__height):
            for cols in range(self.__width):
                rect_ += '#'
            rect_ += '\n'
        return rect_[:-1]
