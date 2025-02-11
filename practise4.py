n = 3
board = [["-" for _ in range(n)] for _ in range(n)]

position = [
    [0, 0], [0, 1], [0, 2],
    [1, 0], [1, 1], [1, 2],
    [2, 0], [2, 1], [2, 2]
]

win_position = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
]

first_symbols_board = []
second_symbols_board = []

for row in board:
    print(" ".join(row))

def first_choice():
    while True:
        column1, row1 = map(int, input("First player: Enter row and column by space: ").split())
        if board[row1][column1] == "+" or board[row1][column1] == "0":
            print("This cell is busy, choose another cell")
        elif [row1, column1] in position:
            board[row1][column1] = "+"
            first_symbols_board.append((row1, column1))
            break
        else:
            print("You chose wrong coordinates, please, try again")

def second_choice():
    while True:
        column2, row2 = map(int, input("Second player: Enter row and column by space: ").split())
        if board[row2][column2] == "+" or board[row2][column2] == "0":
            print("This cell is busy, choose another cell")
        elif [row2, column2] in position:
            board[row2][column2] = "0"
            second_symbols_board.append((row2, column2))
            break
        else:
            print("You chose wrong coordinates, please, try again")

def check_win():
    for win_comb in win_position:
        if all(coord in first_symbols_board for coord in win_comb):
            print("First player won!")
            return True
        elif all(coord in second_symbols_board for coord in win_comb):
            print("Second player won!")
            return True
    return False

while True:
    first_choice()
    for row in board:
        print(" ".join(row))
    if check_win():
        break

    second_choice()
    for row in board:
        print(" ".join(row))
    if check_win():
        break

