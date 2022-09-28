#!/usr/bin/python3
"""More Class Base"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle"""
    def __init__(self, size, height):
        """Constructor and width height"""
        self.__size = size
        self.__height = height
        BaseGeometry.integer_validator(self, "size", self.__size)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__size * self.__height

    def __str__(self):
        """Print"""
        return ("[Rectangle] " + str(self.__size) + "/" + str(self.__height))
