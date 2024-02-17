#!/usr/bin/python3
"""
text must be a string, otherwise raise a TypeError exception with the\
message text must be a string
There should be no space at the beginning or at the end of each printed line
"""

def text_indentation(text):
    """
    a function that prints a text with 2 new lines after each of\
    these characters: ., ? and :
    """
    """ raise error for non string input """
    if type(text) != str:
        raise TypeError("text must be a string")

    """ make a list of the delimiters """
    delimi = ['.', '?', ':']

    """ Iterate through the characters """
    for item in range(len(text)):
        if text[item] in delimi:
            print("{}{}".format(text[item], "\n"))

        elif text[item] == ' ':
            if text[item - 1] not in delimi:
                print(" ", end="")

        else:
            print("{}".format(text[item]), end="")
