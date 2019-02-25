class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if (not obstacleGrid) or (obstacleGrid[0][0] == 1):
            return 0
        row = len(obstacleGrid)
        colum = len(obstacleGrid[0])
        res = [[0 for i in range(colum)] for j in range(row)]  
        for i in range(row):
            for j in range(colum):
                if (i == 0  and j == 0):
                    res[i][j] = 1
                    continue
                if (obstacleGrid[i][j] == 1):
                    res[i][j] = 0
                else:   
                    res[i][j] = 0
                    if (i > 0):
                        res[i][j] += res[i - 1][j]
                    if (j > 0): 
                        res[i][j] += res[i][j - 1]
        return res[row -1][colum - 1]         
if __name__ == '__main__':
    grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
    ]
    res = Solution()
    ans = res.uniquePathsWithObstacles(grid)
    print(ans)

                

        