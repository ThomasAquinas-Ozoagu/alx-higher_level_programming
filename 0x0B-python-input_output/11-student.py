#!/usr/bin/python3
""" Student to JSON with filter"""


class Student:
    """ a class Student that defines a student by: (based on 9-student.py) """
    def __init__(self, first_name="", last_name="", age=0):
        """ class Instantiation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """  retrieves a dictionary representation of a Student instance """
        if attrs:
            half = {}
            if "age" in attrs:
                half["age"] = self.age
            if "last_name" in attrs:
                half["last_name"] = self.last_name
            if "first_name" in attrs:
                half["first_name"] = self.first_name

            return half

        return {"age": self.age, "last_name": self.last_name,
                "first_name": self.first_name}

    def reload_from_json(self, json):
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
