class Solution(object):
    def maxUncrossedLines(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(len(B) + 1)] for j in range(len(A) + 1)]
        for i in range(len(A) + 1):
            for j in range(len(B) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                else:
                    # if A[i] == B[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1 if A[i - 1] == B[j - 1] else dp[i - 1][j - 1]
                    dp[i][j] = max(dp[i][j], dp[i - 1][j], dp[i][j - 1])
        return dp[len(A)][len(B)]