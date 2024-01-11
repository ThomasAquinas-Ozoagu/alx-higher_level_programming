#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if b > a:
            if b > 1:
                print(", ", end="")
            print("{:d}{:d}".format(a, b), end="")
print("\n", end="")
