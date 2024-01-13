#!/usr/bin/python3
for al in range(ord('Z'), ord('A') - 1, -1):
    print("{}".format(chr(al) if (al % 2 == 1) else chr(al + 32)), end="")
