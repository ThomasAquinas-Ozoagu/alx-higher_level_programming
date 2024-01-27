#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = []
    sum = 0
    new = list(map(lambda x: x if x in uniq else uniq.append(x), my_list))
    for y in uniq:
        sum += y
    return (sum)
