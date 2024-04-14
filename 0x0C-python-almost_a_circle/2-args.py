#!/usr/bin/python3
if __name__ == "__main__":
    import sys
count = 1
lenght = len(sys.argv)

print("{} argument{}{}{}".format(lenght - 1, "" if lenght == 2 else "s",
                                 "." if lenght == 1 else "",
                                 ":" if lenght > 1 else ""))

while count < lenght:
    print("{}: {}".format(count, sys.argv[count]))
    count += 1
