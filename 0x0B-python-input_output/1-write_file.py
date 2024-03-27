#!/usr/bin/python3
""" Read file and print the content to standard output """


def write_file(filename="", text=""):
    """ A function that writes a string to a text file (UTF8) and\
    returns the number of characters written """
    with open(filename, 'w', encoding="utf-8") as f:
        amount = f.write(text)
    return amount
