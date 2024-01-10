#!/usr/bin/python3
if __name__ == "__main__"
import sys
total = 0
for y in range(len(sys.argv) - 1):
    total += int(sys.argv[y + 1])
print("{}".format(total))
