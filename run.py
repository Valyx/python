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

while ships > 0:

    def random_row(board):
        return randint(0, len(board) - 1)

    def random_col(board):
        return randint(0, len(board[0]) - 1)

    ship_row = random_row(board)
    ship_col = random_col(board)

    """ function to check if a ship is already present in that specific point"""

    if (board[ship_row][ship_col]) == "O":
        board[ship_row][ship_col] = "@"
        ships = ships + 1

for turn in range(9):
    print ("Turn"), turn

    """ checks in input is correct"""
    input = False

    def isNumber(s):
        for i in range(len(s)):
            if s[i].isdigit() != True:
                return False
        return True

    while input == False:
            guess_row = int(input("Guess Row:"))
            guess_col = int(input("Guess Col:"))
        if isNumber(guess_row) and isNumber(guess_col):
            print("Target aquired")
            input = True
        else:
            print("Those coordinates don't look correct, sir")

    if guess_row == ship_row and guess_col == ship_col:
        print("Nice hit captain!")
        ships = ships - 1
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("You're probably aiming for another dimension mate!")
        elif(board[guess_row][guess_col] == "X"):
            print("We already check that area sir !")
        else:
            print("You will get them the next time !!")
            board[guess_row][guess_col] = "X"
    if turn == 8:
        print("Game Over")
    if ships == 0:
        print("Congratultions ! We've wipped out the enemy!")
        break
    turn = +1
    print_board(board)
