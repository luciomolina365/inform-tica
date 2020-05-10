# Reversegam: a clone of Othello/Reversi
import random
import sys
WIDTH =  # Board is  spaces wide
HEIGHT =  # Board is  spaces tall
def drawBoard(board):
    # Print the board passed to this function Return None
    print('  ')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+))
    print(' +--------+')
    print('  ')

def getNewBoard():
    # Create a brand-new, blank board data structure
    board = []
    for i in range(WIDTH):
        boardappend([' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
    return board

def isValidMove(board, tile, xstart, ystart):
    # Return False if the player's move on space xstart, ystart is
        invalid
    # If it is a valid move, return a list of spaces that would become
        the player's if they made a move here
    if board[xstart][ystart] != ' ' or not isOnBoard(xstart, ystart):
        return False

    if tile == 'X':
        otherTile = 'O'
    else:
        otherTile = 'X'

    tilesToFlip = []
    for xdirection, ydirection in [[, ], [, ], [, ], [, -],
        [, -], [-, -], [-, ], [-, ]]:
        x, y = xstart, ystart
        x += xdirection # First step in the x direction
        y += ydirection # First step in the y direction
        while isOnBoard(x, y) and board[x][y] == otherTile:
            # Keep moving in this x & y direction
            x += xdirection
            y += ydirection
            if isOnBoard(x, y) and board[x][y] == tile:
                # There are pieces to flip over Go in the reverse
                    direction until we reach the original space, noting all
                    the tiles along the way
            while True:
                x -= xdirection
                y -= ydirection
                if x == xstart and y == ystart:
                    break
                tilesToFlipappend([x, y])

    if len(tilesToFlip) == : # If no tiles were flipped, this is not a
        valid move
        return False
    return tilesToFlip

def isOnBoard(x, y):
    # Return True if the coordinates are located on the board
    return x >=  and x <= WIDTH -  and y >=  and y <= HEIGHT -

def getBoardWithValidMoves(board, tile):
    # Return a new board with periods marking the valid moves the player
        can make
    boardCopy = getBoardCopy(board)

    for x, y in getValidMoves(boardCopy, tile):
        boardCopy[x][y] = ''
    return boardCopy

def getValidMoves(board, tile):
    # Return a list of [x,y] lists of valid moves for the given player
        on the given board
    validMoves = []
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if isValidMove(board, tile, x, y) != False:
                validMovesappend([x, y])
    return validMoves

def getScoreOfBoard(board):
    # Determine the score by counting the tiles Return a dictionary
        with keys 'X' and 'O'
    xscore =
    oscore =
    for x in range(WIDTH):
        for y in range(HEIGHT):
            if board[x][y] == 'X':
                xscore +=
            if board[x][y] == 'O':
                oscore +=
    return {'X':xscore, 'O':oscore}

def enterPlayerTile():
    # Let the player enter which tile they want to be
    # Return a list with the player's tile as the first item and the
        computer's tile as the second
    tile = ''
    while not (tile == 'X' or tile == 'O'):
        print('Do you want to be X or O?')
        tile = input()upper()

    # The first element in the list is the player's tile, and the second
        is the computer's tile
    if tile == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def whoGoesFirst():
    # Randomly choose who goes first
    if randomrandint(, ) == :
        return 'computer'
    else:
        return 'player'

def makeMove(board, tile, xstart, ystart):
    # Place the tile on the board at xstart, ystart and flip any of the
        opponent's pieces
    # Return False if this is an invalid move; True if it is valid
    tilesToFlip = isValidMove(board, tile, xstart, ystart)

    if tilesToFlip == False:
        return False

    board[xstart][ystart] = tile
    for x, y in tilesToFlip:
        board[x][y] = tile
    return True

def getBoardCopy(board):
    # Make a duplicate of the board list and return it
    boardCopy = getNewBoard()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            boardCopy[x][y] = board[x][y]

    return boardCopy

def isOnCorner(x, y):
    # Return True if the position is in one of the four corners
    return (x ==  or x == WIDTH - ) and (y ==  or y == HEIGHT - )

def getPlayerMove(board, playerTile):
    # Let the player enter their move
    # Return the move as [x, y] (or return the strings 'hints' or
        'quit')
    DIGITSTO = '       'split()
    while True:
        print('Enter your move, "quit" to end the game, or "hints" to
            toggle hints')
        move = input()lower()
        if move == 'quit' or move == 'hints':
            return move

        if len(move) ==  and move[] in DIGITSTO and move[] in
            DIGITSTO:
            x = int(move[]) -
            y = int(move[]) -
            if isValidMove(board, playerTile, x, y) == False:
                continue
            else:
                break
        else:
            print('That is not a valid move Enter the column (-) and
                then the row (-)')
            print('For example,  will move on the top-right corner')

    return [x, y]

def getComputerMove(board, computerTile):
    # Given a board and the computer's tile, determine where to
    # move and return that move as an [x, y] list
    possibleMoves = getValidMoves(board, computerTile)
    randomshuffle(possibleMoves) # Randomize the order of the moves

    # Always go for a corner if available
    for x, y in possibleMoves:
        if isOnCorner(x, y):
            return [x, y]

    # Find the highest-scoring move possible
    bestScore = -
    for x, y in possibleMoves:
        boardCopy = getBoardCopy(board)
        makeMove(boardCopy, computerTile, x, y)
        score = getScoreOfBoard(boardCopy)[computerTile]
        if score > bestScore:
            bestMove = [x, y]
            bestScore = score
    return bestMove

def printScore(board, playerTile, computerTile):
    scores = getScoreOfBoard(board)
    print('You: %s points Computer: %s points' % (scores[playerTile],
        scores[computerTile]))

def playGame(playerTile, computerTile):
    showHints = False
    turn = whoGoesFirst()
    print('The ' + turn + ' will go first')

    # Clear the board and place starting pieces
    board = getNewBoard()
    board[][] = 'X'
    board[][] = 'O'
    board[][] = 'O'
    board[][] = 'X'

    while True:
        playerValidMoves = getValidMoves(board, playerTile)
        computerValidMoves = getValidMoves(board, computerTile)

        if playerValidMoves == [] and computerValidMoves == []:
            return board # No one can move, so end the game

        elif turn == 'player': # Player's turn
            if playerValidMoves != []:
                if showHints:
                    validMovesBoard = getBoardWithValidMoves(board,
                        playerTile)
                    drawBoard(validMovesBoard)
                else:
                    drawBoard(board)
                printScore(board, playerTile, computerTile)

                move = getPlayerMove(board, playerTile)
                if move == 'quit':
                    print('Thanks for playing!')
                    sysexit() # Terminate the program
                elif move == 'hints':
                    showHints = not showHints
                    continue
                else:
                    makeMove(board, playerTile, move[], move[])
            turn = 'computer'

        elif turn == 'computer': # Computer's turn
            if computerValidMoves != []:
                drawBoard(board)
                printScore(board, playerTile, computerTile)

                input('Press Enter to see the computer's move')
                move = getComputerMove(board, computerTile)
                makeMove(board, computerTile, move[], move[])
            turn = 'player'



print('Welcome to Reversegam!')

playerTile, computerTile = enterPlayerTile()

while True:
    finalBoard = playGame(playerTile, computerTile)

    # Display the final score
    drawBoard(finalBoard)
    scores = getScoreOfBoard(finalBoard)
    print('X scored %s points O scored %s points' % (scores['X'],
        scores['O']))
    if scores[playerTile] > scores[computerTile]:
        print('You beat the computer by %s points! Congratulations!' %
            (scores[playerTile] - scores[computerTile]))
    elif scores[playerTile] < scores[computerTile]:
        print('You lost The computer beat you by %s points' %
            (scores[computerTile] - scores[playerTile]))
    else:
        print('The game was a tie!')

    print('Do you want to play again? (yes or no)')
    if not input()lower()startswith('y'):
        break