#!/usr/bin/python3
"""More class base"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        """Instantiation with size"""
        self.__size = size
        super().__init__(self.__size, self.__size)
