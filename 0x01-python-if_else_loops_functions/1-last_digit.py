#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    lastnumber = number % -10
else:
    lastnumber = number % 10
if lastnumber > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lastnumber))
elif lastnumber < 6 and lastnumber != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lastnumber))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
