#!/usr/bin/python3
import random
num = random.randint(-10000, 10000)
if num < 0:
    lastdigit = num % -10
else:
    lastdigit = num % 10
if lastdigit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
            .format(number, lastdigit))
elif lastdigit < 6 and lastdigit != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
            .format(number, lastdigit))
else:
    print("Last digit of {:d} is 0 and is 0".format(number))
