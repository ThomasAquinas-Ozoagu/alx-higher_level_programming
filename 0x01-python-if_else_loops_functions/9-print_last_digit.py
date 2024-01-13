#!/usr/bin/python3
def print_last_digit(number):
    y = 1
    if number < 0:
        y = -1

    z = number * y

    if z > 999:
        z = z % 1000
    if z > 99:
        z = z % 100
    if z > 9:
        z = z % 10

    print(z, end="")
    return(z)
