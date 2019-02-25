class Solution():
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        if (row == 0):
            return 0    
        colum = len(grid[0])
        if (row == 0 or colum == 0):
            return 0 
        for i in range(row):
            for j in range(colum):
                if (i == 0 and j == 0):
                    continue
                else:
                    if i == 0:
                        grid[i][j] = grid[i][j - 1] + grid[i][j]
                    elif j == 0:
                        grid[i][j] = grid[i - 1][j] + grid[i][j]
                    else:
                        grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[row - 1][colum - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
res = Solution()
ans = res.minPathSum(grid)
print(ans);        