#!/usr/bin/python3
""" Module of Student Class
"""


class Student:
    """ Student Class
    """
    def __init__(self, first_name, last_name, age):
        """ init function

            Args:
                first_name (str): first name
                last_name (str): second name
                age (int): age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ function that retrieve a dictionary rep of a Student instance
            Args:
                attrs (list): filter of strings
            Returns:
                (dict): dictonray rep
        """
        if not attrs:
            return self.__dict__
        else:
            return [attr for attr in self.__dict__ if attr in attrs]
