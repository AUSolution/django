# A guessing game
# Enter a number between 1 & 99
# The computer will try to guess it
# Let the computer know if it is too high or too low



from random import randint

number = input('Think of a secret number between 1 & 99: ')
print("Enter 'h' if the computer's guess is too high.")
print("Enter 'l' if the computer's guess is toon low.")
print("Enter 'c' if the computer's guessed correct.")

h = 100
l = 1
comp_guess = randint(l, h)
#print("The computer's first guess is {}".format(comp_guess))
count = 1
print('Tries: {}'.format(count))
while comp_guess != number:
    print()
    print("The computer guessed {}: ".format(comp_guess))
    print('Is the guess too high or too low? h or l')
    response = str(input().lower())
    #while response != 'h' or response != 'l' or response != 'c':
#        print('ERROR: Please enter a valid high, low response: ')
#        response = input('h or l?').lower()
    if response == 'h':
        h = comp_guess - 1
        print('The new high is {}'.format(h))
    elif response == 'l':
        l = comp_guess + 1
        print('The new low is {}'.format(l))
    elif response == 'c':
        break
    comp_guess = randint(l, h)
    count += 1

print('The computer guessed your numer: {} on the {} attempt.'.format(number, count))

