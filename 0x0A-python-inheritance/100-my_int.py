#!/usr/bin/python3
"""Module that defines a class MyInt inheriting from int."""


class MyInt(int):
    """A rebel integer class that inverts comparison operators."""

    def __eq__(self, other):
        """Override the equality operator to invert its behavior."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator to invert its behavior."""
        return super().__eq__(other)
