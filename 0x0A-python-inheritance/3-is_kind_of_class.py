#!/usr/bin/python3
"""Same class of inherit from"""


def is_kind_of_class(obj, a_class):
    """A function that returns True if the object
    is an instance of, or if the object is an instacne
    of a class that inherited from, the specified class;
    otherwise returns False
    
    Args:
        obj(any): Object of the class
        a_class(type): describes the class
    """
    if isinstance(obj, a_class):
        return True
    return False
