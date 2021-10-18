from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print(" ".join(row))

"""
starting the game and printing the board
"""

print ("The hunt in on!")
print_board(board)

"""
generating random positions for the ships
"""
ships = 4

Do while ships >= 0:

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    """ function to check if a ship is already present in that specific point"""
    
    if board[ship_row,ship_col] == O:
        board[ship_row,ship_col] == @
        ships = ships + 1

