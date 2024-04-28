#!/usr/bin/python3
""" My fist class for testing """
import json


class Base:
    """ The base class """
    __nb_objects = 0

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is None or list_objs == []:
            return []
        newlist = []
        for x in range(len(list_objs)):
            newlist.append(list_objs[x].to_dictionary())

        with open('{}.json'.format(cls.__name__), "w") as file:
            file.write(Base.to_json_string(newlist))

    def __init__(self, id=None):
        """ initializes class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return []
        return json.dumps(list_dictionaries)
