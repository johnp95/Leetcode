def uniquePaths(r,c):
    if r== 1 or c == 1 : return 1
    down = uniquePaths(r-1,c)
    right = uniquePaths(r,c-1)
    return down + right
def uniquePaths2(r,c,curr='',idx=0):
    if r == 1 and c ==1 : 
        print(curr)
        return 
    if r > 1:
        uniquePaths2(r-1,c,curr+' down',idx+1)
    if c > 1:
        uniquePaths2(r,c-1,curr+' right',idx+1)
def uniquePaths3(r,c,curr=''):
    if r == 1 and c ==1 : 
        return [curr]
    ans = []
    if r > 1:
        ans += uniquePaths3(r-1,c,curr+'D')
    if c > 1:
        ans += uniquePaths3(r,c-1,curr+'R')
    return ans
def uniquePathsDiag(r,c,curr=''):
    if r == 1 and c == 1 : 
        print(curr)
        return 
    if r > 1:
        uniquePathsDiag(r-1,c,curr+'D' + ' ')
    if c > 1:
        uniquePathsDiag(r,c-1,curr+'R'+ ' ')
    if r > 1 or c > 1:
        uniquePathsDiag(r-1,c-1,curr+'Diag' + ' ')
def mazeObstacles(matrix):
    memo = {}
    def helper(r,c):
        if (r,c) in memo : return memo[(r,c)]
        rBounds =  0 <= r < len(matrix)
        cBounds =  0 <= c < len(matrix[0])
        if not rBounds or not cBounds : return 0 
        if matrix[r][c] == 1 : return 0
        if r == len(matrix)-1 and c == len(matrix[0])-1 : return 1
        down = helper(r+1,c)
        right = helper(r,c+1)
        memo[(r,c)] =  down + right
        return memo[(r,c)]
    return helper(0,0)
def allPaths(matrix):
    def helper(r,c,curr=''):
        if r == len(matrix)-1 and c == len(matrix[0])-1: 
            print(curr,matrix)
            return
        if not matrix[r][c] : return 
        matrix[r][c] = False

        if r < len(matrix)-1 : 
            helper(r+1,c,curr + 'D')
        if c < len(matrix[0])-1:
            helper(r,c+1,curr+'R')
        if r > 0:
            helper(r-1,c,curr+'U')
        if c > 0:
            helper(r,c-1,curr+'L')
        matrix[r][c] = True
def allPathsPrint(matrix):
    path = [[0]*len(matrix[0]) for _ in range(len(matrix))]
    def helper(r,c,path,step,curr='',):
        if r == len(matrix)-1 and c == len(matrix[0])-1: 
            path[r][c] = step
            for i in path:
                print(i)
            print(curr)
            print()
            return
        if not matrix[r][c] : return 
        matrix[r][c] = False
        path[r][c] = step
        if r < len(matrix)-1 : 
            helper(r+1,c,path,step+1,curr + 'D')
        if c < len(matrix[0])-1:
            helper(r,c+1,path,step+1,curr+'R')
        if r > 0:
            helper(r-1,c,path,step+1,curr+'U')
        if c > 0:
            helper(r,c-1,path,step+1,curr+'L')
        matrix[r][c] = True
        path[r][c] = 0

    return helper(0,0,path,1)
if __name__ == '__main__':
    # allPaths([[True,True,True],[True,True,True],[True,True,True]])
    allPathsPrint([[True,True,True],[True,True,True],[True,True,True]])
       