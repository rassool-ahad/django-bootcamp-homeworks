#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
    print("run the program again and this time enter your scores")
    exit()
numbers = sys.argv[1:]
try:
    print(f"your average is {sum(map(int, numbers)) / len(numbers)}")
except:
    raise Exception("invalid numbers ")
