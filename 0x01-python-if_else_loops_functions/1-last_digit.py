#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
nos = str(number)
z = nos[-1]
x = int(z)
if x > 5:
    print(f"Last digit of {number} is {x} and is greater than 5")

elif x == 0:
    print(f"Last digit of {number} is {x} and is 0")

else:
    print(f"Last digit of {number} is {x} and is less than 6 and not 0")