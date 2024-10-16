#!/usr/bin/python3
"""Module to define a function that adds attributes to objects."""


def add_attribute(obj, attribute, value):
    """Attempt to add a new attribute to an object if allowed.

    Raises:
        TypeError: If the object cannot have new attributes.
    """
    # Check if the object allows new attributes
    if not isinstance(obj, object) or not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    
    # Set the new attribute
    setattr(obj, attribute, value)
