""" What are the odds? The gods determine your fate.

Let's see what they have determined for you."""

from random import randint
from time import sleep

print ("Welcome to what are the odds? A game to decide your fate.")
sleep(1)

def whatOdds(theOdds):
    while theOdds <= 1 or theOdds > 20:
        print ("The odds must be between 2 & 20")
        theOdds = int(input("What are the odds? "))
    computer_guess = randint(1, theOdds)  #Randint creates a random variable between 1 & theOdds
    print ("Guess a number between 1 and " + str(theOdds))
    sleep(1)
    user_guess = int(input("Guess a number: "))
    while user_guess <= 1 or user_guess > theOdds:
        print("Don't be a fucking cheater.")
        print ("Guess a number between 1 and " + str(theOdds))
        user_guess = int(input("Guess again fucker: "))
    print ("Awaiting your Fate...")
    sleep(2)
    print ("Our Guess: %s" % (computer_guess))
    sleep(.5)
    if user_guess == computer_guess:  #or guess_again == computer_guess:
        print ("Go Get Em Tiger!")
        return
    else:
        print ("Not Today Junior.")
        return

whatOdds(input("What are the Odds? "))


"""
Possibile Features:
Restart button after guess.
Slider for Odds, easier than typing.
History.
Share with amigos
"""
