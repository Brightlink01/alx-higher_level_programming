#!/usr/bin/python3

""" the module for list class inheritANCE"""

class MyList(list):
    """ inherits from the list base class and implements
        sorted printing
    """

    def print_sorted(self):
        """ prints the list sorted in ascending order """
        print(sorted(self))
