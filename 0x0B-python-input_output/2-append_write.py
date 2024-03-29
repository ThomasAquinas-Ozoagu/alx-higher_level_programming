#!/usr/bin/python3
""" Read file and print the content to standard output """


def append_write(filename="", text=""):
    """ A function that writes a string to a text file (UTF8) and\
    returns the number of characters written """
    with open(filename, 'a', encoding="utf-8") as f:
        amount = f.write(text)
    return amount
