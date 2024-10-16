#!/usr/bin/python3
"""Module that defines a Rectangle class inheriting from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents a rectangle using properties and methods from BaseGeometry."""

    def __init__(self, width, height):
        """
        Initialize a new Rectangle instance.

        Parameters:
        - width (int): The width of the rectangle (must be a positive integer).
        - height (int): The height of the rectangle (must be a positive integer).
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculate and return the area of the rectangle.

        Returns:
        - The area (int) as the product of width and height.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Return a string representation of the Rectangle.

        This will be in the format:
        [Rectangle] <width>/<height>
        """
        return f"[Rectangle] {self.__width}/{self.__height}"
