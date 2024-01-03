#!/usr/bin/python3
def uppercase(str):
    for y in str:
        if ord(y) >= 97 and ord(y) <= 122:
            y = chr(ord(y) - 32)
        print("{}".format(y), end="")
    print()
