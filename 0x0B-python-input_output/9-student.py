#!/usr/bin/python3
""" Student to JSON """


class Student:
    def __init__(self, first_name="", last_name="", age=0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return {"first_name": self.first_name,
                "last_name": self.last_name, "age": self.age}
