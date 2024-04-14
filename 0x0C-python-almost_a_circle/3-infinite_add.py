#!/usr/bin/python3
if __name__ == "__main__":
    import sys
count = 1
sum = 0
lenght = len(sys.argv)

while count < lenght:
    sum += int(sys.argv[count])
    count += 1

print("{}".format(sum))
