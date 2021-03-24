board = [
   [7, 8, 0, 4, 0, 0, 1, 2, 0],
   [6, 0, 0, 0, 7, 5, 0, 0, 9],
   [0, 0, 0, 6, 0, 1, 0, 7, 8],
   [0, 0, 7, 0, 4, 0, 2, 6, 0],
   [0, 0, 1, 0, 5, 0, 9, 3, 0],
   [9, 0, 4, 0, 6, 0, 0, 0, 5],
   [0, 7, 0, 3, 0, 0, 0, 1, 2],
   [1, 2, 0, 0, 0, 7, 4, 0, 0],
   [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-----------------------------")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print ("|", end = " ")
            if j == 8:
                print (board[i][j])
            else:
                print (str(board[i][j]) + " ", end = " ")


def find_blanks(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None

def is_valid (board, input, position):
    #Check row validity
    for i in range(len(board[0])):
        if board[position[0]] [i] == input and position[1] != i:
            return False
    #Check column valiidty
    for i in range(len(board[0])):
        if board[i] [position[1]] == input and position[0] != i:
            return False
    #Check box validity
    box_x = position[1] // 3
    box_y = position[0] // 3
    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if board[i][j] == input and (i,j) != position:
                return False
    return True

def backtracking(board):
    find = find_blanks(board)
    if not find:
        return True
    else:
        row, column = find

    for i in range(1, 10):
        if is_valid(board, i, (row, column)):
            board [row][column] = i
            if backtracking(board):
                return True
            board [row][column] = 0
    return False

print_board(board)
backtracking(board)
print("SOLVED")
print_board(board)