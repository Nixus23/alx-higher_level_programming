#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv)
    count -= 1
    result = 0

    if count == 0:
        print("{}".format(count))
    else:
        for i in range(1, len(argv)):
            result += int(argv[i])
        print("{}".format(result))
