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
        dic = self.__dict__
        if not attrs:
            return dic
        else:
            return {attr: dic[attr] for attr in attrs if attr in dic}
