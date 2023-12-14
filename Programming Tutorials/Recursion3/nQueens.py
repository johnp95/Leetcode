def solveNQueens(n):
    board  = [[False]*n for _ in range(n)]
    def helper(board,row):
        if row == len(board):
            display(board)
            print()
            return 1
        count = 0
        for col in range(len(board)):
            if isSafe(board,row,col):
                board[row][col] = True
                count += helper(board,row+1)
                board[row][col] = False
        return count
    return helper(board,0)

def display(board):
    for row in board:
        for element in row:
            if element:
                print("Q ",end='')
            else:
                print("X ",end='')
        print()
def isSafe(board,row,col):
    for i in range(len(board)):
        if board[i][col]:
            return False
    maxLeft = min(row,col)
    for i in range(1,maxLeft+1):
        if board[row-i][col-i]:
            return False

    maxRight = min(row,len(board)-col-1)
    for i in range(1,maxRight+1):
        if board[row-i][col+i]:
            return False

    return True

if __name__ == '__main__':
    n = 4
    solveNQueens(n)