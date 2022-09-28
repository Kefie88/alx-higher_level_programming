#!/usr/bin/python3
"""Student to JSON"""


class Student:
    """Represent a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new student

        Args:
            first_name (str): The first name of the student
            last_name (str): The last name of the student
            ag (int): The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Gets a dictionary representation of the student"""
        return self.__dict__
