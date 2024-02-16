"""
first_name and last_name must be strings otherwise,
raise a TypeError exception with the message first_name must be a string or
last_name must be a string
"""


def say_my_name(first_name, last_name=""):
    """
    a function that prints My name is <first name> <last name>
    """

    """ checks if first name is a string """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    """ checks if last name is a string """
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    """ puts your name on STDOUT """
    print("My name is {} {}".format(first_name, last_name))
