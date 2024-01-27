#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):
    sorted_list = list(a_dictionary)
    sorted_list.sort()
    for x in sorted_list:
        print("{}: {}".format(x, a_dictionary[x]))
