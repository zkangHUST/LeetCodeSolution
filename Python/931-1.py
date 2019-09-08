class Solution:
    def minFallingPathSum(self, A: List[List[int]]) -> int:
        dp = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        for j in range(len(A[0])):
            dp[0][j] = A[0][j]
        for i in range(1, len(A)):
            for j in range(len(A[0])):
                if j == 0:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
                elif j == len(A[0]) - 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + A[i][j]
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i - 1][j + 1]) + A[i][j]
        return min(dp[-1])                    