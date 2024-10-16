#!/usr/bin/python3
"""Module that defines the BaseGeometry class with basic geometry functionality."""


class BaseGeometry:
    """A blueprint class for geometric shapes, with methods for future expansion."""

    def area(self):
        """
        Raises an Exception to indicate that the area method is not implemented.

        This should be overridden by any subclass that has a specific area calculation.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that `value` is a positive integer.

        Parameters:
        - name (str): The name of the parameter (for error messages).
        - value (int): The value to validate.

        Raises:
        - TypeError: If `value` is not an integer.
        - ValueError: If `value` is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
