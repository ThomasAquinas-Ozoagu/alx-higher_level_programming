#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    e = 0
    f = 0
    while(e < x):
        try:
            print("{:d}".format(my_list[e]), end="")
            f += 1
        except (ValueError, TypeError):
            print("", end="")
        e += 1
    print()
    return (f)
