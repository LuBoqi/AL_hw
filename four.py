import copy
import random

boardSize = 3
boardSize__ = boardSize ** 2
solutionNum = 0
solutionMaxNum = 1


def is_valid(board, row, col, num):
    for i in range(boardSize__):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = boardSize * (row // boardSize), boardSize * (col // boardSize)
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i + start_row][j + start_col] == num:
                return False

    return True


def solve_sudoku(board, isTest=False):
    empty_cell = find_empty_cell(board)
    if not empty_cell:
        if isTest:
            return True
        global solutionNum
        solutionNum = solutionNum + 1
        print('the', solutionNum, 'solution:')
        print_board(board)
        if solutionNum > solutionMaxNum - 1:
            return True
        return False
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board, isTest):
                return True
            board[row][col] = 0
    return False


def find_empty_cell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(board):
    for i in range(len(board)):
        if i % boardSize == 0 and i != 0:
            print("- -" * boardSize__)
        for j in range(len(board[0])):
            if j % boardSize == 0 and j != 0:
                print("| ", end="")
            print(board[i][j], end=" ")
        print()
    print()


def generate_sudoku():
    print('generating board......')
    generateBoard = [[0] * boardSize__ for _ in range(boardSize__)]
    for _ in range(random.randint(int(0.15 * boardSize__ ** 2), int(0.3 * boardSize__ ** 2))):
        row, col, num = (random.randint(0, boardSize__ - 1),
                         random.randint(0, boardSize__ - 1),
                         random.randint(1, boardSize__))
        while not is_valid(generateBoard, row, col, num) or generateBoard[row][col] != 0:
            row, col, num = (random.randint(0, boardSize__ - 1),
                             random.randint(0, boardSize__ - 1),
                             random.randint(1, boardSize__))
        generateBoard[row][col] = num
    testBoard = copy.deepcopy(generateBoard)
    if solve_sudoku(testBoard, True):
        return generateBoard
    else:
        return generate_sudoku()


if __name__ == "__main__":
    # boardSize = eval(input('please input the board size:'))
    question = generate_sudoku()
    print('the initial board is：')
    print_board(question)
    solve_sudoku(question)
    if not solutionNum:
        print('No solution!')
