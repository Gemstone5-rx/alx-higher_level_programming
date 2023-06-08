#!/usr/bin/python3

import sys

if __name__ == "__main__":
    # variable to hold the final result
    result = 0
    for arg in sys.argv[1:]:
        result += int(arg)

    print(result)
