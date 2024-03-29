#!/usr/bin/python3
""" Create object from a JSON file """
import json


def load_from_json_file(filename):
    """ a function that creates an Object from a JSON file """
    with open(filename, encoding="utf-8") as f:
        new_data = f.read()

    return json.loads(new_data)
