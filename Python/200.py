class Solution:
    def numIslands(self, grid):
        ans = 0
        book = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" and book[i][j] == 0:
                    self.dfs(grid, i, j, book)
                    ans += 1
        return ans
        
    def dfs(self, grid, i, j, book):
        if grid[i][j] == "0" or book[i][j] == 1:
            return 
        book[i][j] = 1
        if i - 1 >= 0:
            self.dfs(grid, i - 1, j, book)
        if i + 1 < len(grid):
            self.dfs(grid, i + 1, j, book)
        if j - 1 >= 0:
            self.dfs(grid, i, j - 1, book)
        if j + 1 < len(grid[0]):
            self.dfs(grid, i, j + 1, book)

# land = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
land = [["1","1","1"],["0","1","0"],["0","1","0"]]

p = Solution()
ans = p.numIslands(land)
