#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    new_dict = {}
    for x in a_dictionary:
        new_dict[x] = 2 * a_dictionary[x]
    return (new_dict)
