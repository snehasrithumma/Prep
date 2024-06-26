def safe(board, row, col):
    print('-------------', row, col)
    for i in range(row):
        print('row', i, col)
        if board[i][col] == 1: 
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        print('colums', row, j)
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, len(board), 1)):
        print('diagonal', i, j)
        if board[i][j] == 1:
            return False
    return True



def solve_n_queens_board(board, row):
    if row>= len(board):
        return True
    for col in range(len(board)):
        print('&&&&&&&&&&&&&&&&&&', row, col, board)
        if safe(board, row, col):
            board[row][col] = 1
            print('&&&&&&&&&&&&&&&&&&', row+1, col, board)
            if solve_n_queens_board(board, row+1):
                return True
            print('failed', row, col)
            board[row][col] = 0
    return False



def solve_n_queens(n):
    board = [[0]*n for _ in range(n)]
    print(board)
    if solve_n_queens_board(board, 0):
        return board
    else:
        return None




# Example usage
n = 4
solution = solve_n_queens(n)
print('*******************')
if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists for N =", n)