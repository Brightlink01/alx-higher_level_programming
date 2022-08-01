#!/usr/bin/python3

def inherits_from(obj, a_class):
    """ returns True if obj is an instance
        of a class or instance of a subclass
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
