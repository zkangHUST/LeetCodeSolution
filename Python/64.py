class Solution():
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid)
        # 防止输入grid == []
        if (row == 0):
            return 0    
        # 防止输入grid == [[]]
        colum = len(grid[0])
        if (row == 0 or colum == 0):
            return 0
        res = [[0 for i in range(colum)] for j in range(row)] 
        for i in range(row):
            for j in range(colum):
                if (i == 0 and j == 0):
                    res[i][j] = grid[0][0]
                else:
                    if i == 0:
                        res[i][j] = res[i][j - 1] + grid[i][j]
                    elif j == 0:
                        res[i][j] = res[i - 1][j] + grid[i][j]
                    else:
                        res[i][j] = min(res[i - 1][j], res[i][j - 1]) + grid[i][j]
        return res[row - 1][colum - 1]

grid = [[1,3,1],[1,5,1],[4,2,1]]
res = Solution()
ans = res.minPathSum(grid)
        