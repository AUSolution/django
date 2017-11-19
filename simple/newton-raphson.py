epsilon = 0.01

root  = 2.0 #float(input('What root do you want to find: '))
y = float(input('Enter a number to find the Square Root of: '))
guess = y/float(root)
numGuesses = 1

print()
print('I will find the square root of {}'.format(int(y)))
print('My first guess is {}'.format(guess))
print()

while abs(guess**root - y) >= epsilon:
  numGuesses += 1
  guess = guess - (((guess**root) - y) /(root*guess))
  print('Guess #: {} is {}'.format(numGuesses, guess))


print('numGuesses = {}'.format(numGuesses))
print('Square root of {} is about {}'.format(y, guess))
