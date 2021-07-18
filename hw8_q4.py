#!/usr/bin/env python3
import argparse
import random as rnd

my_parser = argparse.ArgumentParser(description="guess number")
my_parser.add_argument('-f', '--fromnumber', action="store", type=int, required=True)
my_parser.add_argument('-t', '--tonumber', action="store", type=int, required=True)
my_parser.add_argument('-g', '--guessnumber', action="store", type=int, required=True)
args = my_parser.parse_args()

print("z")
fromnumber = args.fromnumber
tonumber = args.tonumber
guesses = args.guessnumber
rnd_num = rnd.randint(fromnumber, tonumber)
counter = 0
while counter != guesses:
    try:
        inp = int(input(f"you have {guesses - counter} tries to go .enter your guess:"))
    except:
        print("enter valid number")
        continue
    if inp < rnd_num:
        print(f"its bigger than {inp}")
    elif inp > rnd_num:
        print(f"its lower than {inp}")
    elif inp == rnd_num:
        print("you win :)")
        exit()
    counter += 1
else:
    print("you loose :(")
