#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add_num = 0
    for i in range(len(sys.argv) - 1):
        add_num += int(sys.argv[i + 1])
    print("{}".format(add_num))
