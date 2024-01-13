#!/usr/bin/python3
def fizzbuzz():
    for a in range(1, 101):
        print("{} ".format("FizzBuzz" if (a % 15 == 0)
                           else ("Buzz" if (a % 5 == 0)
                                 else ("Fizz" if (a % 3 == 0)
                                       else a))),
              end="")
