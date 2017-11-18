""" What are the odds? The gods determine your fate. 

Let's see what they have determined for you."""

# -*- coding: utf-8 -*-

from random import randint
from time import sleep

print ("Welcome to what are the odds. A game to decide your fate.")
print ("You determine your odds. Choose a number between 1 and your odd.")
sleep(1)
print ("If our guess matches yours then it's game time.")
print ("Else, you live to see another day.")
sleep(1)


def get_user_guess():
	user_guess = int(input("Guess a number: "))
        
def whatOdds(theOdds):
	computer_guess = randint(1, theOdds) #creates a random variable between 1 & theOdds
	print ("The maximum possible value is: " + str(theOdds))
	sleep(2)
	user_guess = get_user_guess() 
“””	While user_guess <=1 and user_guess > theOdds:
		print(“Your guess is not acceptable”)
		user_guess = get_user_guess()
“””
	print ("Awaiting your Fate...")
	sleep(1)
	print ("Our Guess: %s" % (computer_guess))
	sleep(1)
	if user_guess == computer_guess:
		print ("Go Get Em Tiger!")
		return
	else:
		print ("Not Today Junior.")
		return

whatOdds(int(input("What are the Odds: ")))


#	Possibile Features:
#	Restart button after guess.
#	Slider for Odds, easier than typing.
#	History?
#	Share
