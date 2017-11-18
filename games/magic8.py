import random
messages = ['It is certain', 'It is decidely so', 'Yes definitely', 'Ehh', 'Ask Later', 'Probs not', "Doesn't look good", 'Fuck Naw']
def ball8(n):
  print(messages[n])

def main():
  print ('Magic 8 Ball results: ')
  for x in range(5):
    ball8(random.randint(0, len(messages) - 1))
 
# a terrible long and awful 8ball program
def getAnswer(answerNumber):
	if answerNumber == 1:
		return (“It is certain”)
	elif answerNumber ==2:
		return ‘It is decidedly so’
	elif answerNumber ==3:
		return ‘Yes’
	elif answerNumber ==4:
		return ‘Reply hazy, try again.’
	elif answerNumber ==5:
		return ‘Ask again later.’
	elif answerNumber ==6:
		return ‘Concentrate and ask again.’
	elif answerNumber ==7:
		return ‘My reply is no’
	elif answerNumber ==8:
		return ‘Outlook not so good’
	elif answerNumber ==9:
		return ‘Very doubtful’
r = random.randint(1, 9)
fortune = answerNumber(r)
print(fortune)


if __name__ == '__main__':
    main()

grid = [['.','.','.','.','.','.'],
        ['.','o','o','.','.','.'],
        ['o','o','o','o','.','.'],
        ['o','o','o','o','o','.'],
        ['.','o','o','o','o','o'],
        ['o','o','o','o','o','.'],
        ['o','o','o','o','.','.'],
        ['.','o','o','.','.','.'],
        ['.','.','.','.','.','.']]
def gridd(grid):
  for y in range(6):
    for x in range(0, 8):
        print (grid[x][y], end='')
    print(grid[0][y])
    

gridd(grid)
