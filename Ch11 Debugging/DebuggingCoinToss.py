# This code is taken from the book. The exercise was to debug the program.

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()

# Commented out the following line, as the input is in the form of a string but this selects an integer
# toss = random.randint(0, 1) # 0 is tails, 1 is heads

# Replaced with this block to appropriately reflect the input
toss = random.choice(('heads','tails'))

if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    # guesss = input() - commented out this line as it's incorrect; the variable "guesss" is a typo, should be "guess"
    guess = input()
    if toss == guess:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')