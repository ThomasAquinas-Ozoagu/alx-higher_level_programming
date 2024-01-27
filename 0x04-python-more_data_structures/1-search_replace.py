#!/usr/bin/python3


def search_replace(my_list, search, replace):

    new = list(map(lambda x, y=search, z=replace:
                   z if x == y else x, my_list))
    return(new)
