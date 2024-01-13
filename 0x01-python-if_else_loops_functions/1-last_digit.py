#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
y = 1
if number < 0:
    y = -1
    z = -1 * number
else:
    z = number

if z > 999:
    z = z % 1000
if z > 99:
    z = z % 100
if z > 9:
    z = z % 10

z *= y

if z > 5:
    print("Last digit of {:d} is {:d} and is greater than 5".format(number, z))

elif z == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, z))

else:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, z))
