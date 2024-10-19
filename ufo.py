def initBoard():
    board = [[' ' for _ in range(7)] for _ in range(7)]

    return board

def piecePlacement(board):
    shipPosition = checkInput("Enter a number from 1-7 for the placement of the ship: ", 1, 7) - 1
    board[6][shipPosition] = 'S'

    ufoPosition = checkInput("Enter a number from 1-7 for the placement of the UFO: ", 1, 7) - 1
    board[0][ufoPosition] = 'U'

    return shipPosition, ufoPosition

def checkInput(question, minVal, maxVal):
    while True:
        try:
            val = int(input(question))
            if minVal <= val <= maxVal: return val
            print(f"Please enter a number from {minVal} to {maxVal}")

        except ValueError:
            print("Invalid input. Please enter a number.")

def movePlayer(board, row, col, direction, player):
    if (direction == 1 and col < 6):
        if (player == 'U' and board[row][col + 1] == 'M'): # move right
            board[row][col] = ' '
        else:
            board[row][col] = ' '
            col += 1
            board[row][col] = player

    elif (direction == 2 and col > 0):
        if (player == 'U' and board[row][col - 1] == 'M'): # move left
            board[row][col] = ' '
        else:
            board[row][col] = ' '
            col -= 1
            board[row][col] = player

    elif (direction == 3 and row < 6): # move down
        if (board[row + 1][col] == 'M'):
            board[row][col] = ' '
        else:
            board[row][col] = ' '
            row += 1
            board[row][col] = player
    
    displayBoard(board)
    if (player == 'U'): winner(board, row, col)
    return row, col

def updateMissiles(board, shipCol, ufoRow, ufoCol):
    missileRow = None

    for i in range(len(board) - 1):
        if ('M' in board[i][shipCol]):
            board[i][shipCol] = ' '
            missileRow = i
            if i > 0:
                board[i - 1][shipCol] = 'M'
                displayBoard(board)
                winner(board, ufoRow, ufoCol)
            return shipCol

    missileRow = 5
    board[missileRow][shipCol] = 'M'

    displayBoard(board)
    winner(board, ufoRow, ufoCol)

    return shipCol

def winner(board, ufoRow, ufoCol):
    if (ufoRow >= 6): # UFO reached the bottom of the board before ship got to it
        print("Team UFO won!")
        exit()
    elif (ufoRow == 6 and board[ufoRow][ufoCol] == 'S'): # check to see if UFO hit the ship
        print("Team UFO won! The UFO hit the ship!")
        exit()

    for i in board:
        if 'U' in i: return False

    print("Team Ship won! The UFO was hit by a missile!")
    exit()

def displayBoard(board):
    for row in board: print(row)

def main():
    board = initBoard()
    shipCol, ufoCol = piecePlacement(board)
    missileCounter, shipRow, ufoRow = 0, 6, 0

    displayBoard(board)
    while True:
        shipDirection = checkInput("What would the ship like to do? Enter 1 to go right, 2 to go left, 3 to shoot: ", 1, 3)
        if (shipDirection == 1 or shipDirection == 2): shipRow, shipCol = movePlayer(board, shipRow, shipCol, shipDirection, 'S')
        
        elif (shipDirection == 3):
            if (missileCounter < 20):
                shipCol = updateMissiles(board, shipCol, ufoRow, ufoCol)
                missileCounter += 1
            else: print("You've reached the missile shooting limit. Please choose a different action")

        ufoDirection = checkInput("What would the UFO like to do? Enter 1 to go right, 2 to go left, 3 to go down: ", 1, 3)
        ufoRow, ufoCol = movePlayer(board, ufoRow, ufoCol, ufoDirection, 'U')

if __name__ == "__main__":
    main()