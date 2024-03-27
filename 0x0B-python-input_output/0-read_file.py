#!/usr/bin/python3
""" Read file and print the content to standard output """


def read_file(filename=""):
    """ a function that reads a text file (UTF8) and prints it to stdout """
    with open(filename, encoding="utf-8") as f:
        new_data = f.read()

    print(new_data, end="")
