#!/usr/bin/python3
""" Technical interview preparation """


def pascal_triangle(n):
    """returns list of lists of integers representing Pascal’s triangle of n"""
    if n <= 0:
        return []
    x = 1
    outer = []
    """ print("outer is now ", outer)"""
    while x <= n:
        """print("\n\n\n starting... \nx is now", x)"""
        inner = []
        y = 1
        while y <= x:
            """print("xy is now", x, y)"""
            if y == 1:
                if x == 1:
                    inner = [1]
                    y += 1
                    """print("inner is now", inner)"""
                    continue
                """if x == 2:
                    inner = [1, 1]
                    y += 1
                    print("inner is now", inner)
                    continue"""
                inner = [1]
                """print("After {}=1 = {} --> {}".format(y, inner, outer))"""
                y += 1
                continue

            if y == x:
                inner.append(1)
                """print("After {}={} = {} --> {}".
                format(x, y, inner, outer))"""
                y += 1
                continue
            """print("before long append and I am {}{} = {} --> {}"
            .format(x, y, inner, outer))"""
            inner.append(outer[x-2][y-2] + outer[x-2][y-1])
            y += 1
        """print("before outer append and I am {}{} = {} --> {}"
        .format(x, y, inner, outer))"""
        outer.append(inner)
        x += 1
        """print("after we appended and I am {}{} = {} --> {}"
        .format(x, y, inner, outer))"""
        """print(outer)"""
    return outer
