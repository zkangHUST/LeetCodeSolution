class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        self.ans = 0
        visited = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                if grid[i][j] == -1:
                    visited[i][j] = -1
                if grid[i][j] == 1:
                    m, n = i, j
        self.dfs(grid, visited, m, n)
        
        return self.ans
    def dfs(self, grid, visited, i, j):
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0:
            return 
        if grid[i][j] == 2:
            visited[i][j] = 1
            for i in range(len(visited)):
                for j in range(len(visited[0])):
                    if visited[i][j] == 0:
                        return
            self.ans += 1
            return 
        if grid[i][j] == -1:
            visited[i][j] = -1
            return
        if visited[i][j] == 1:
            return
        if grid[i][j] == 0 or grid[i][j] == 1:
            visited[i][j] = 1
            self.dfs(grid, visited, i + 1, j)
            self.dfs(grid, visited, i - 1, j)
            self.dfs(grid, visited, i, j + 1)
            self.dfs(grid, visited, i, j - 1)
            visited[i][j] = 0
        return 
            
            
    