#!/usr/bin/python3
""" this method contains a function that
    returns all attributes and methods of an object
"""


def lookup(obj):
    """ return all available
        attributes obj(object) - object to get attribtes and methods from.
    """
    return dir(obj)
