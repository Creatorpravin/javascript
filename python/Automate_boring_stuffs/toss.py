#! python3
# coin-toss.py
# Author: Kene Udeh
# Source: Automate the Boring stuff with python Ch. 10 Project

import random

if __name__ == "__main__":

    guess = ''
    options = ['tails', 'heads']

    while guess not in ('heads', 'tails'):
        print('Guess the coin toss! Enter heads or tails:')
        guess = input()

    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if guess == options[toss]:
        print('You got it!')
    else:
        print('Nope! Guess again!')
        guess = input()
        toss = random.randint(0 ,1) # Re-declare it here for more intrest
        if guess == options[toss]:
            print('You got it!')
        else:
            print('Nope. You are really bad at this game.')