#!/usr/bin/python3
"""More Class Base"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a rectangle"""
    def __init__(self, width, height):
        """Constructor and width height"""
        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", self.__width)
        BaseGeometry.integer_validator(self, "height", self.__height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        """Print"""
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))
