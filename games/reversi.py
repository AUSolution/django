# reversi as prescribed in inventwithpython
# http://bit.ly/2A8r36R

import random
import sys

def drawBoard(board):
    #This function prints out the baord
    #that it was passed. Returns None.
    HLINE = '+---+---+---+---+---+---+---+---+'
    VLINE = '  |   |   |   |   |   |   |   |   |'

    print(' 1 2 3 4 5 6 7 8')
    print(HLINE)

    #the foot loop will interate 1 time for each rows, so 8 total.
    #
    for y in range(8):
        print(VLINE)
        print(y+1, end='')
        for x in range(8):
            print('I {}',format(board[x][y], end=''))
        print('I')
    print(VLINE)
    print(HLINE)

def resetBoard(board):
    #Reset board
    for x in range(8):
        for y in range(8):
            board[x][y]= ''
    #starting pieces:
    board[3][3] = 'X'
    board[3][4] = 'O'
    board[4][3] = 'O'
    board[4][4] = 'X'

def getNewBoard():
    #Creates a brand new, blank board data structure
    board = []
    for i in range(8):
        board.append([''] * 8)

    return board

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
        x, y = xstart, ystart
        x += xdirection # first step in the direction
        y += ydirection # first step in the direction
        if isOnBoard(x, y) and board[x][y] == otherTile:
            #There is a piece belonging to
            #the other player next to our piece
            x += xdirection
            y += ydirection
            if not isOnBoard(x, y):
                continue
            while board[x][y] == otherTile:
                x += xdirection
                y += ydirection
                if not isOnBoard(x, y):
                    break
            if not isONBoard(x, y):
                continue
            if board[x][y] == tile:
                #there are pieces to flip over.
                #Go in the reverse direction until
                #we reach the original space
                #noting all the tiles along the way
                while True:
                    x -= xdirection
                    y -= ydirection
                    if x == xstart and y == ystart:
                        break
                    tilesToFlip.append([x, y])
    board[xstart][ystart] = '' #restore empther space
    if len(tilesToFlip) == 0:
        return False
    return tilesToFlip

def isOnBoard(x, y):
    #returns a list of [x, y] lists of valid moves
    #for the given player on the given board
    validMoves = []

    for x in range(8):
        for y in range(8):
            if isValidMove(board, tile, x, y) != False:
                validMoves.append([x, y])
    return ValidMoves
def getScoreOfBoard(board):
    #determine the score by counting the tiles.
    #returns a dictionary with keys 'X' and 'O'
    xscore = 0
    oscore = 0
    for x in range(8):
        for y in range(8):
            if board[x][y] == 'X':
                xscore += 1
                if board[x][y] == 'O':
                    oscore += 1
    return {'X':xscore, 'O':oscore}

def enterPayerTile():
    #Lets teh player type which tile they to be
    #Returns a list with the player's tile as the
    #first item, and the computer's tile as teh second
    tile = ''
    while not (tile =='X' or tile =='O'):
        print('Do you want tot he X or O?')
        tile = input().upper()
    #the first element in the list is the player's tile,
    #the second is the computer's tile
        if tile == 'X':
            return['X', 'O']
        else:
            return['O', 'X']

def whoGoesFirst():
    #Random choose the player who goes first
    if random.randint(0,1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    # This function returns True if teh player
    # wants to play gain, otherwise it returns False
    print('Do you want to play again? yes or no')
    return input().lower().startswith('y')

def makeMove(board, tile, xstart, ystart):
    #Place the tile on the board at xstart, ystart
    # and flip any of the opponent's pieces
    tilesToFlip == isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] - tile
    return True

def getBoardCopy(board):
    #make a duplicate of the board list and return the duplicate
    dupeBoard = getNewBoard()

    for x in range(8):
        for y in range(8):
            dipeBOard[x][y] = board[x][y]
    return dopeBoard

def isONCorner(x, y):
    #returns true if the position is in one of the four corners
    return (x==0 and y ==0) or (x == 7 and y == 0) or (x == 7 and y == 7)

def getPlayerMove(board, playerTile):
    #Let the player type in theri move
    #Retursn teh move as [x,y ] or returns the strings hint or quit
    DIGITS1TO8 = '1 2 3 4 5 6 7 8'.split()
    while True:
        print('Enter  your move, or type quit to end the game, or hints to turn off/on hints.')
        move = input().lower()
        if move == 'quit':
            return 'quit'
        if move == 'hints':
            return 'hints'
        if len(move) ==2 and move[0] in DIGITS1TO8 and move[1] in DIGITS1TO8:
            x = int(move[0]) - 1
            y =int(move[1]) -1
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move. Type the x and y coordinates.')
            print('For example, 81 will be the top-right corner')
    return [x, y]

def getComputerMove(board, computerTile):
    #Given aboard and teh computer's tile determine where to
    #move and return that move as a [x, y] list
    possibleMoves = getValidMoves(board, computerTile)

    #randomize the order of possible moves
    random.shuffle(possibleMoves)

    #always got for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]
        










            
