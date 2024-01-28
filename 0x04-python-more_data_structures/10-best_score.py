#!/usr/bin/python3


def best_score(a_dictionary):
    if a_dictionary == {} or a_dictionary is None:
        return None
    keys = list(a_dictionary)
    bigg = a_dictionary[keys[0]]
    bigKey = keys[0]

    for x in keys:
        if a_dictionary[x] > bigg:
            bigg = a_dictionary[x]
            bigKey = x

    return (bigKey)
