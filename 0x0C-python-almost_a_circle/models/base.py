#!/usr/bin/python3
""" Module of Base class
"""


class Base:
    """ Base class for all other classes
        to manage id attribute of sub classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """ init method for objects of this class

           Args:
                id (int) : id of object
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ function that returns JSON representation

            Args:
                list_dictionaries (list of dictionaries): list of dict

            Returns:
                (str): JSON representation of object
        """
        import json
        if list_dictionaries is not None and len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ function that writes JSON string representation of list of
            objects to file

            Args:
                list_objs (list of objects): list of objects to be written
                to file
        """
        filename = "{}.json".format(cls.__name__)
        with open(filename, mode='w', encoding="utf-8") as fi:
            ls_dict = []
            if list_objs:
                for obj in list_objs:
                    ls_dict.append(obj.to_dictionary())
            fi.write(Base.to_json_string(ls_dict))

    @staticmethod
    def from_json_string(json_string):
        """ funcitons that returns the list of json string representation

            Args:
                json_string (str): string representing a list of
                                    dictionaries
            Returns:
                (list of dictionaries): list of dictionaries
        """
        import json
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set
        """
        obj = cls(1, 1, 0, 0, 100)
        obj.update(**dictionary)
        return obj
