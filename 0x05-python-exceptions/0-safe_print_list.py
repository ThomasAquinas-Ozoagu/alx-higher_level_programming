#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    e = 0
    while(e < x):
        try:
            print("{}".format(my_list[e]), end="")
        except IndexError:
            break
        e += 1
    print()
    return (e)
