#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, which is a special case of a rectangle."""

    def __init__(self, size):
        """
        Initialize a new Square instance.

        Parameters:
        - size (int): The size of the square sides (must be a positive integer).
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Return a string representation of the Square.

        This will be in the format:
        [Square] <size>/<size>
        """
        return f"[Square] {self.__size}/{self.__size}"
