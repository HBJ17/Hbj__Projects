import numpy

board = numpy.array([['-','-','-'],['-','-','-'],['-','-','-']])

pl1 = 'X'
pl2 = 'O'

def check_rows(symbol):
    for r in range(3):
        if all(board[r][c] == symbol for c in range(3)):
            print(symbol, "Won")
            return True
    return False

def check_col(symbol):
    for c in range(3):
        if all(board[r][c] == symbol for r in range(3)):
            print(symbol, "Won")
            return True
    return False

def check_dia(symbol):
    if board[0][0] == board[1][1] == board[2][2] == symbol:
        print(symbol, "Won")
        return True
    if board[0][2] == board[1][1] == board[2][0] == symbol:
        print(symbol, "Won")
        return True
    return False

def won(symbol):
    return check_rows(symbol) or check_col(symbol) or check_dia(symbol)

def play(symbol):
    print(numpy.matrix(board))
    while True:
        row = int(input("Enter row position (1/2/3) = "))
        col = int(input("Enter col position (1/2/3) = "))
        if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == '-':
            board[row-1][col-1] = symbol
            break
        else:
            print("Invalid input, please try again.")

def place():
    for turn in range(9):
        if turn % 2 == 0:
            print("X's Turn")
            play(pl1)
            if won(pl1):
                return
        else:
            print("O's Turn")
            play(pl2)
            if won(pl2):
                return
    print("Draw!!")

place()
