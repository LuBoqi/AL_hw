import copy
import random

# 定义棋盘大小
boardSize = 3
# 计算棋盘大小平方
boardSize__ = boardSize ** 2
# 初始化解数
solutionNum = 0
# 最大解数
solutionMaxNum = 1


# 判断位置是否有效
def is_valid(board, row, col, num):
    # 判断当前行列是否有效
    for i in range(boardSize__):
        if board[row][i] == num or board[i][col] == num:
            return False
    # 判断当前区块是否有效
    start_row, start_col = boardSize * (row // boardSize), boardSize * (col // boardSize)
    for i in range(boardSize):
        for j in range(boardSize):
            if board[i + start_row][j + start_col] == num:
                return False
    return True


# 解棋盘
def solve_sudoku(board, isTest=False):
    # 查找空格位置
    empty_cell = find_empty_cell(board)
    # 判断是否解开
    if not empty_cell:
        # 判断是否为测试
        if isTest:
            return True
        # 解数加一
        global solutionNum
        solutionNum = solutionNum + 1
        # 打印解
        print('the', solutionNum, 'solution:')
        print_board(board)
        # 判断解数是否满足最大解数需求
        if solutionNum > solutionMaxNum - 1:
            return True
        return False
    else:
        # 获取空格位置
        row, col = empty_cell
    # 循环判断数字是否有效
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            # 将数字放入空格
            board[row][col] = num
            # 递归判断能否解开
            if solve_sudoku(board, isTest):
                return True
            # 回溯
            board[row][col] = 0
    return False


# 查找空格位置
def find_empty_cell(board):
    # 遍历棋盘
    for i in range(len(board)):
        for j in range(len(board[0])):
            # 判断是否为空格
            if board[i][j] == 0:
                return (i, j)
    return None


# 打印棋盘
def print_board(board):
    # 遍历棋盘
    for i in range(len(board)):
        # 判断是否换行区块
        if i % boardSize == 0 and i != 0:
            print("- -" * boardSize__)
        # 遍历列
        for j in range(len(board[0])):
            # 判断是否换列区块
            if j % boardSize == 0 and j != 0:
                print("| ", end="")
            # 打印数字
            print(board[i][j], end=" ")
        print()
    print()


# 生成棋盘
def generate_sudoku():
    print('generating board......')
    # 初始化棋盘
    generateBoard = [[0] * boardSize__ for _ in range(boardSize__)]
    # 添加随机个数数字
    for _ in range(random.randint(int(0.15 * boardSize__ ** 2), int(0.3 * boardSize__ ** 2))):
        # 随机生成空格位置
        row, col, num = (random.randint(0, boardSize__ - 1),
                         random.randint(0, boardSize__ - 1),
                         random.randint(1, boardSize__))
        # 判断是否有效
        while not is_valid(generateBoard, row, col, num) or generateBoard[row][col] != 0:
            # 随机再生成空格位置
            row, col, num = (random.randint(0, boardSize__ - 1),
                             random.randint(0, boardSize__ - 1),
                             random.randint(1, boardSize__))
        # 将数字放入空格
        generateBoard[row][col] = num
    # 复制棋盘
    testBoard = copy.deepcopy(generateBoard)
    # 判断是否可解
    if solve_sudoku(testBoard, True):
        return generateBoard
    else:
        return generate_sudoku()


if __name__ == "__main__":
    # 输入棋盘大小（弃用）
    # boardSize = eval(input('please input the board size:'))
    # 生成棋盘
    question = generate_sudoku()
    # 打印题目棋盘
    print('the initial board is：')
    print_board(question)
    # 解
    solve_sudoku(question)
    # 判断是否有解
    if not solutionNum:
        print('No solution!')
