#!/usr/bin/python3
"""Singly linked list module."""


class Node:
    """Class that defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes the node with data and the next node.

        Args:
            data (int): The data of the node.
            next_node (Node, optional): The next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the data of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node.

        Args:
            value (Node or None): The next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Class that defines a singly linked list."""

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node in the correct sorted position.

        Args:
            value (int): The value to insert in the linked list.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data >= new_node.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        
        current = self.__head
        while current.next_node is not None and current.next_node.data < new_node.data:
            current = current.next_node
        
        new_node.next_node = current.next_node
        current.next_node = new_node

    def __str__(self):
        """Return a string representation of the list."""
        current = self.__head
        output = []
        while current is not None:
            output.append(str(current.data))
            current = current.next_node
        return "\n".join(output)
