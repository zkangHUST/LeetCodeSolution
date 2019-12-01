class Solution:
    def __init__(self):
        self.valid = True
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    continue
                self.valid = True
                self.dfs(grid, i, j)
                if self.valid:
                    ans += 1
        return ans
        
    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            self.valid = False
            return 
        if grid[x][y] == 1:
            return
        grid[x][y] = 1
        self.dfs(grid, x - 1, y)
        self.dfs(grid, x + 1, y)
        self.dfs(grid, x, y - 1)
        self.dfs(grid, x, y + 1)
    

grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]

p = Solution()

ans = p.closedIsland(grid)

print(ans)