#!/usr/bin/python3
"""module for singly linked list"""


class Node:
    """defines a node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes the singly linked list"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = None

    @property
    def data(self):
        """gets data attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """Sets data attribute"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """gets next_node attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets next_node attribute"""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """Initializes the singly linked list"""
        self.head = None

    def sorted_insert(self, value):
        """inserts a new node with the given value into
        the linked list"""
        new_node = Node(value)
        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while (current.next_node is not None and
                   value >= current.next_node.data):
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """provides a string representation of the linked list"""

        result = []
        current = self.head
        while current is not None:
            result.append(str(current.data))
            current = current.next_node
        return '\n'.join(result)
