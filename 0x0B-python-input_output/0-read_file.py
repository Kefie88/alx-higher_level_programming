#!/usr/bin/python3
"""Read File"""


def read_file(filename=""):
    """A function that reads a text file (UTF8)
    and prints it to stdout

    Args:
        filename(any): name of the file
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
