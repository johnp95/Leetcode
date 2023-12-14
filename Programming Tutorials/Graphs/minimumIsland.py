from collections import defaultdict
def islandCount(grid):
    minSize = float('inf')
    visited = set()
    for r in range(len(grid)): 
        for c in range(len(grid[0])):
            size = explore(grid,r,c,visited)
            if size > 0 and size < minSize:
                minSize = size
    return minSize            
def explore(grid,r,c,visited):
    rowInbouds = 0 <= r < len(grid)
    colInbouds = 0 <= c < len(grid[0])
    if not rowInbouds or not colInbouds : return 0
    if grid[r][c] == 'W' : return 0
    pos = (r,c)
    if pos in visited : return 0
    visited.add(pos)
    size = 1
    size += explore(grid,r-1,c,visited)
    size += explore(grid,r+1,c,visited)
    size += explore(grid,r,c-1,visited)
    size += explore(grid,r,c+1,visited)

    return size
    
if __name__ == '__main__':
    grid = [
  ["W","L","W","W","W"],
  ["W","L","W","W","W"],
  ["W","W","W","L","W"],
  ["L","W","W","L","L"],
  ["L","L","W","W","W"],
    ]
    print(islandCount(grid))