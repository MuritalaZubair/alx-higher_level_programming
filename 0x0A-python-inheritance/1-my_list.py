#!/usr/bin/python3
"""Defines a class MyList that inherits from the built-in list class."""


class MyList(list):
    """A custom list class with an additional method to print the list sorted in ascending order."""
    
    def print_sorted(self):
        """
        Prints the elements of the list in ascending order.
        
        This does not modify the original list; it simply displays a sorted version.
        """
        print(sorted(self))
