#!/usr/bin/python3
"""More class base"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size):
        """Size init"""
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(self.__size, self.__size)

    def __str__(self):
        return ("[Square] " + str(self.__size) + "/" + str(self.__size))
