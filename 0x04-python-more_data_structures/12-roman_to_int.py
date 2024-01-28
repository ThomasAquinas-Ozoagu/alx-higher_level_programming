#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string == "":
        return (0)

    sum = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for a in roman_string:
        if conv[a] > sum:
            sum = conv[a] - sum
        else:
            sum += conv[a]
    return (sum)
