#!/usr/bin/python3
"""Module that provides linkeds list

Classes:
    Node: defines a node in linked list
    SinglyLinkedList: defines a single linked list
"""


class Node:
    """Node class
    Attributes:
        __data (int): data contained in node
        __next_node (Node): reference to next node
        ...
    """
    def __init__(self, data, next_node=None):
        """Initializes a new instance of the class.

        Args:
        data (int): data of node
        next_node (Node): reference to next node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter of data attribute
        Returns:
            int: data of node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """setter of data attribute.

        Args:
        value (int): size of square.
        """
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """getter of next_node attribute
        Returns:
            Node: next node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """setter of next_node attribute.

        Args:
        value (Node): next node
        """
        if type(value) is Node or value is None:
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """SinglyLinkedList class
    Attributes:
        __head (int): data contained in node
    """
    def __init__(self):
        """ Initialize new instance of object
        """
        self.__head = None

    def sorted_insert(self, value):
        """ insert node and keep the list sorted

        Args:
            value (Node): node to be added
        """

        trav = self.__head
        # create new node
        print("inserting {}".format(value))
        new_node = Node(value)
        if trav is None:
            self.__head = new_node
        elif value < trav.data:
            self.__head = new_node
            new_node.next_node = trav
        else:
            prev = self.__head
            while trav and value >= trav.data:
                prev = trav
                trav = trav.next_node
            # link prev to new node
            new_node.next_node = trav
            prev.next_node = new_node

    def __str__(self):
        """ to be printed by print

        Returns(str): list of all values
        """
        result = ""
        trav = self.__head
        while trav:
            result += str(trav.data)
            if trav.next_node:
                result += '\n'
            trav = trav.next_node
        return result
