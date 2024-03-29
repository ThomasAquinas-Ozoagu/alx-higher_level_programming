#!/usr/bin/python3
""" Save Object to a file """
import json


def save_to_json_file(my_obj, filename):
    """ a function that writes an Object to a text file,
    using a JSON representation """

    text = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        amount = f.write(text)
