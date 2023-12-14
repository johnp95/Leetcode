from collections import defaultdict
def islandCount(grid):
    visited = set()
    count = 0
    for r in range(len(grid)): 
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited):
                count += 1
    return count
            
def explore(grid,r,c,visited):
    rowInbouds = 0 <= r < len(grid)
    colInbouds = 0 <= c < len(grid[0])
    if not rowInbouds or not colInbouds : return False
    if grid[r][c] == 'W' : return False
    # pos = str(r) + ',' + str(c)
    pos = (r,c)
    if pos in visited : return False
    visited.add(pos)
    explore(grid,r-1,c,visited)
    explore(grid,r+1,c,visited)
    explore(grid,r,c-1,visited)
    explore(grid,r,c+1,visited)

    return True
    
if __name__ == '__main__':
    grid = [
  ["W","L","W","W","W"],
  ["W","L","W","W","W"],
  ["W","W","W","L","W"],
  ["L","W","W","L","L"],
  ["L","L","W","W","W"],
    ]
    print(islandCount(grid))