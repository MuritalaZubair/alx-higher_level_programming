#!/usr/bin/python3
"""Defines a BaseGeometry class with a method to be implemented."""


class BaseGeometry:
    """A class that serves as a blueprint for geometric shapes."""

    def area(self):
        """
        Raises an Exception indicating that the area method is not yet implemented.

        This method is intended to be overridden by subclasses.
        """
        raise Exception("area() is not implemented")
