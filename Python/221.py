class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        ans = 0
        dp = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] != '1':
                    dp[i][j] = 0
                else:
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                         dp[i][j] = self.check(matrix, dp, i, j) + 1
                if dp[i][j] > ans:
                    ans = dp[i][j]
                
        return ans * ans
    def check(self, matrix, dp, m, n):
        a, b = 0, 0
        for i in range(m -1, m - dp[m - 1][n - 1] - 1, -1):
            if matrix[i][n] != '1':
                break
            else:
                a += 1
        
        for j in range(n - 1, n - dp[m - 1][n - 1] - 1, -1):
            if matrix[m][j] != '1':
                break
            else:
                b += 1 
        return min(a, b, dp[m - 1][n - 1])


matrix = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]

p = Solution()

ans = p.maximalSquare(matrix)