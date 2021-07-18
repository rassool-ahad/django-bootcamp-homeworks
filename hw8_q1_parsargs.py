#!/usr/bin/env python3

import argparse
import random as rnd
my_parser = argparse.ArgumentParser(description="guess number")
my_parser.add_argument('-g', '--grades', action="store", type=int,nargs='*', required=True)
my_parser.add_argument('-f', '--float', action="store", type=int, required=False, default=2)
args = my_parser.parse_args()
grades = args.grades
fl = args.float
avg: float = sum(grades) / len(grades)
print(round(avg, fl))