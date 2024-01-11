#!/usr/bin/python3
for _m in range(ord('a'), ord('z')+1):
    if _m != ord('e') and _m != ord('q'):
        print("{:c}".format(_m), end="")
