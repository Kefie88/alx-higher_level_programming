#!/usr/bin/python3
"""Only sub class"""


def inherits_from(obj, a_class):
    """A function that returns True if the object is
    an instance of a class that inherited (directly or indirectly)
    from the specified class;
    otherwise returns False

    Args:
        obj(any): object of the class
        a_class(type): describes the class
    """
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
