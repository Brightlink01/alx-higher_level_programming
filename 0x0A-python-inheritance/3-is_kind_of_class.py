#!/usr/bin/python3
# Auth: Tsedal Tsegaye @ Python ALX

""" the function to check whether the instance blongs or not"""

def is_kind_of_class(obj, a_class):
    """ Returns true if object is an instace of a class"""

    if isinstance(obj, a_class):
        return True
    return False
