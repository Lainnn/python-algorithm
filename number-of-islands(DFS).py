def check_bond(x,y,grid):
    if x < len(grid) and y < len(grid[0]) and x >= 0 and y >= 0:
        return True
    else:
        return False
    
def get_nearby(pos,grid):
    x, y = pos
    adj=[]
    if check_bond(x+1,y, grid) == True and grid[x+1][y] == "1":
        adj.append([x+1,y])
    if check_bond(x,y+1,grid) == True and grid[x][y+1] == "1":
        adj.append([x,y+1])
    if check_bond(x-1,y, grid) == True and grid[x-1][y] == "1":
        adj.append([x-1,y])
    if check_bond(x,y-1,grid) == True and grid[x][y-1] == "1":
        adj.append([x,y-1])
    print("adj:")
    print(adj)
    return adj
    
def travel(grid, visited:List[List], pair):
    if str(pair) not in visited:
        visited.add(str(pair))
        adj = get_nearby(pair,grid)
        for i in adj:
            travel(grid,visited,i)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        count = 0
        if len(grid) == 0:
            return 0
        for a in range(len(grid)):
            for b in range(len(grid[0])):
                if grid[a][b] == "1" and str([a,b]) not in visited:
                    x = a
                    y = b
                    count = count + 1
                    print(x,y)
                    travel(grid,visited,[x,y])
        return count
        