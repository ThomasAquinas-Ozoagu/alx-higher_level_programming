#!/usr/bin/python3


def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string == "":
        return (0)

    suma = 0
    conv = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
            'M': 1000}
    for a in range(len(roman_string)):
        if a > 0 and conv[roman_string[a]] > conv[roman_string[a-1]]:
            suma += conv[roman_string[a]]
            suma -= 2*conv[roman_string[a - 1]]
        else:
            suma += conv[roman_string[a]]
    return (suma)
