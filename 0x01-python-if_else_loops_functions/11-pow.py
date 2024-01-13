#!/usr/bin/python3
def pow(a, b):
    c = 1
    if b > 0:
        while (b > 0):
            c *= a
            b -= 1

    if b < 0:
        while (b < 0):
            c /= a
            b += 1

    return (c)
