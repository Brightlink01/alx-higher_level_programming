#!/usr/bin/python3

""" the class objecting checking functions"""

def is_same_class(obj, a_class):
    """ return True if obj is instance of a_class
        otherwise return False
    """
    if type(obj) == a_class:
        return True
    return False
