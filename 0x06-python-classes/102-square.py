#!/usr/bin/python3
"""My square module"""


class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Create a Square.
        
        Args:
            size: length of a side of the Square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the Square.
        
        Raises:
            TypeError: if size is not an integer.
            ValueError: if size is less than 0.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Get the area of the Square.
        
        Returns:
            The area of the Square.
        """
        return self.__size ** 2

    def __le__(self, other):
        return self.area() <= other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __eq__(self, other):
        return self.area() == other.area()
