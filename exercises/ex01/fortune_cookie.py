"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730411526"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint

number_phrase = randint(1,12)
random_phrase = ""

if number_phrase < 4:
    random_phrase = "You will find rekindle an unexpected connection soon."
else:
    if number_phrase > 9:
        random_phrase = "You will see the world in a new way."
    else:
        if number_phrase > 6:
            random_phrase = "Your patience will pay off shortly- do not rush."
        else:
            random_phrase = "Your road to glory will be rocky, but fulfilling."

print("Your fortune cookie says...\n" + random_phrase + "\nNow, go spread positive vibes!")

# Begin your solution here...
